#Copyright [2017] [Alberto Fernandez Comesana]

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

    #http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

import json
import http.client
import http.server
import socketserver

class OpenFDAClient():
    OPENFDA_API_URL = "api.fda.gov"
    OPENFDA_API_EVENT = "/drug/event.json"
    OPENFDA_API_DRUG = "/drug/event.json?search=patient.drug.medicinalproduct="
    OPENFDA_API_COMPANY = "/drug/event.json?search=companynumb="
    def get_event(self, limit):
        conn = http.client.HTTPSConnection(self.OPENFDA_API_URL)
        conn.request("GET", self.OPENFDA_API_EVENT + "?limit=" + limit)
        r1 = conn.getresponse()
        data1 = r1.read()
        data = data1.decode("utf8")
        events = json.loads(data)
        return events

    def get_drug(self, eva):
        conn = http.client.HTTPSConnection(self.OPENFDA_API_URL)
        conn.request("GET", self.OPENFDA_API_DRUG + eva + "&limit=10")
        r1 = conn.getresponse()
        data1 = r1.read()
        data = data1.decode("utf8")
        events_drug = json.loads(data)
        return events_drug

    def get_company(self, eva):
        conn = http.client.HTTPSConnection(self.OPENFDA_API_URL)
        conn.request("GET", self.OPENFDA_API_COMPANY + eva + "&limit=10")
        r1 = conn.getresponse()
        data1 = r1.read()
        data = data1.decode("utf8")
        events_comp = json.loads(data)
        return events_comp

class OpenFDAHTML():
    def get_mainpage(self):
        html = '''
        <html>
            <head>
                <title>OpenFDA Cool App</title>
            </head>
            <body>
                <h1>OpenFDA Client</h1>
                <form method = "get" action = "listDrugs">
                    <input type = "submit" value = "Drugs list">
                    </input>
                    Limit:
                    <input type = "text" name = "limit"></input>
                </form>
                <form method = "get" action = "searchDrug">
                    <input type = "text" name = "drug"></input>
                    <input type = "submit" value = "Company number">
                    </input>
                </form>
                <form method = "get" action = "listCompanies">
                    <input type = "submit" value = "Companies list"></input>
                    Limit:
                    <input type = "text" name = "limit"></input>
                </form>
                <form method = "get" action = "searchCompany">
                    <input type = "text" name = "company"></input>
                    <input type = "submit" value = "Company drugs"></input>
                </form>
                <form method = "get" action = "listGender">
                    <input type = "submit" value = "Patient Sex">
                    </input>
                    Limit:
                    <input type = "text" name = "limit"></input>
                </form>
            </body>
        </html>
        '''

        return html
    def get_mainpage2(self):
        anotherhtml = '''
        <html>
            <head>
                <title>OpenFDA Cool App</title>
            </head>
            <body>
                <h1>OpenFDA Client</h1>
                <form method = "get" action = "drugIndication">
                    <input type = "submit" value = "Drug indication">
                    </input>
                    Limit:
                    <input type = "text" name = "limit"></input>
                </form>
            </body>
        </html>
        '''
        return anotherhtml

    def get_drug_html(self,drugs):
        html_drug = '''
        <html>
            <head>
                <title>Drug List</title>
            </head>
            <body>
                <h1> Drugs </h1>
                <ol>
        '''
        for i in drugs:
            html_drug += '<li>'+i+'</li>'
        html_drug+= '''
                </ol>
            </body>
        </html>
        '''
        return html_drug

    def get_sex_html(self, sex):
        html_sex = '''
        <html>
            <head>
                <title>Patient Sex</title>
            </head>
            <body>
                <h1> Patient Sex </h1>
                <ol>
        '''
        for i in sex:
            html_sex += '<li>'+i+'</li>'
        html_sex+= '''
                </ol>
            </body>
        </html>
        '''
        return html_sex

    def get_company_num_html(self, drugs_company):
        company = []
        company_html = '''
        <html>
            <head>
                <title> Company Numbers </title>
            </head>
            <body>
                <h1> Drug companies </h1>
                <ol>
        '''
        for company in drugs_company:
            company_html += '<li>' + company + '</li>'

        company_html += '''
                </ol>
            </body>
        </html>
        '''
        return company_html

    def get_companies_html(self, company_numbers):
        company = []
        companies_html = '''
        <html>
            <head>
                <title> Companies </title>
            </head>
            <body>
                <h1> Company Numbers </h1>
                <ol>
        '''
        for company in company_numbers:
            companies_html += '<li>' + company + '</li>'
        companies_html += '''
                </ol>
            </body>
        </html>
        '''
        return companies_html
    def get_drugs_from_company_html(self, drugs_comp):
        drug = []
        drugs_comp_html = '''
        <html>
            <head>
                <title> Company drugs </title>
            </head>
            <body>
                <h1> Company drugs </h1>
                <ol>
        '''
        for drug in drugs_comp:
            drugs_comp_html += '<li>' + drug + '</li>'
        drugs_comp_html += '''
                </ol>
            </body>
        </html>
        '''
        return drugs_comp_html

    def get_error_html(self):
        error_html = '''
        <html>
            <head>
                <title> Error 404 </title>
            </head>
            <body>
                <h1> Error 404 </h1>
                <h2> Not found </h2>
            </body>
        </html>
        '''
        return error_html

    def get_indication_html(self, drug_indications):
        indication_html = '''
        <html>
            <head>
                <title> Drug Indications </title>
            </head>
            <body>
                <h1> Drug Indications </h1>
                <ol>
        '''
        for indication in drug_indications:
            indication_html += '<li>' + indication + '</li>'
        indication_html += '''
                </ol>
            </body>
        </html>
        '''
        return indication_html


class OpenFDAParser():
    def get_drugs_from_list(self,events):
        drug_list = []
        for event in events['results']:
            a = event['patient']['drug'][0]['medicinalproduct']
            drug_list.append(a)
        return drug_list

    def get_drug_company(self, events_drug):
        drugs_company = []
        for event in events_drug['results']:
            a = event["companynumb"]
            drugs_company += [a]
        return drugs_company

    def get_company_numbers(self, events_comp):
        company_numbers = []
        for event in events_comp['results']:
            a = event["companynumb"]
            company_numbers += [a]
        return company_numbers

    def get_patient_sex(self, events):
        sex = []
        for i in events['results']:
            a = i['patient']['patientsex']
            sex += [a]
        return sex

    def get_drugs_from_company(self, events_comp):
        drugs_comp = []
        for event in events_comp['results']:
            a = event['patient']['drug'][0]['medicinalproduct']
            drugs_comp += [a]
        return drugs_comp
    def get_drug_indication(self, events):
        drug_indications = []
        for event in events['results']:
            if 'drugindication' in event['patient']['drug'][0]:
                a = event['patient']['drug'][0]['drugindication']
            else:
                a = '-'
            drug_indications +=[a]
        return drug_indications


class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):



    def do_GET(self):
        html = OpenFDAHTML()
        client = OpenFDAClient()
        parser = OpenFDAParser()

        main_page = False
        is_event_drug = False
        is_event_comp = False
        is_search_drug = False
        is_search_comp = False
        is_event_sex = False
        is_error = False
        is_found = False
        is_secret = False
        is_redirect = False
        is_indication = False
        is_another = False

        if self.path == '/':
            main_page = True
            is_found = True
        elif ('/listDrugs') in self.path:
            is_event_drug = True
            is_found = True
        elif ('searchDrug') in self.path:
            eva = self.get_input()
            events_drug = client.get_drug(eva)

            is_search_drug = True
            is_found = True
        elif ('/listCompanies') in self.path:
            is_event_comp = True
            is_found = True
        elif ('searchCompany') in self.path:
            is_search_comp = True
            is_found = True
        elif ('listGender') in self.path:
            is_event_sex = True
            is_found = True
        elif ('another') in self.path:
            is_another = True
            is_found = True
        elif ('drugIndication') in self.path:
            is_indication = True
            is_found = True
        elif "/secret" in self.path:
            is_secret = True
            is_found = True
        elif "/redirect" in self.path:
            is_redirect = True
            is_found = True

        if is_secret:
            self.send_response(401)
            self.send_header("WWW-Authenticate",'Basic realm = "Login required"')
            self.end_headers()
        elif is_redirect:
            self.send_response(302)
            self.send_header("Location", "/")
            self.end_headers()
        elif is_found:
            self.send_response(200)
            self.send_header('Content-type','text/html')

            self.end_headers()
            html2 = html.get_mainpage()
        elif is_another:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()

        else:
            is_error = True
            self.send_response(404)
            self.send_header('Content-type','text/html')
            self.end_headers()
            error_html = html.get_error_html()
            self.wfile.write(bytes(error_html, "utf8"))



        if main_page:
            self.wfile.write(bytes(html2, 'utf8'))
        elif is_event_drug:
            limit = self.get_limit()
            events = client.get_event(limit)
            drugs = parser.get_drugs_from_list(events)
            drug_html = html.get_drug_html(drugs)
            self.wfile.write(bytes(drug_html, "utf8"))
        elif is_search_drug:
            eva = self.get_input()
            events_drug = client.get_drug(eva)
            drugs_company = parser.get_drug_company(events_drug)
            companynumb = html.get_company_num_html(drugs_company)
            self.wfile.write(bytes(companynumb, "utf8"))
        elif is_event_comp:
            limit = self.get_limit()
            events = client.get_event(limit)
            company_numbers = parser.get_company_numbers(events)
            companies_html = html.get_companies_html(company_numbers)
            self.wfile.write(bytes(companies_html, "utf8"))
        elif is_search_comp:
            eva = self.get_input()
            events_comp = client.get_company(eva)
            company_numbers = parser.get_drugs_from_company(events_comp)
            comp_drugs_html = html.get_drugs_from_company_html(company_numbers)
            self.wfile.write(bytes(comp_drugs_html, "utf8"))

        elif is_event_sex:
            limit = self.get_limit()
            events = client.get_event(limit)
            sex = parser.get_patient_sex(events)
            sex_html = html.get_sex_html(sex)
            self.wfile.write(bytes(sex_html, "utf8"))

        elif is_another:
            anotherhtml = html.get_mainpage2()
            self.wfile.write(bytes(anotherhtml, "utf8"))
        elif is_indication:
            limit = self.get_limit()
            events = client.get_event(limit)
            drug_indication = parser.get_drug_indication(events)
            indication_html = html.get_indication_html(drug_indication)
            self.wfile.write(bytes(indication_html, "utf8"))
        return


    def get_input(self):
        eva = self.path.split('=')[1]
        return eva

    def get_limit(self):
        limit = self.path.split('=')[1]
        if limit == '':
            limit = '10'
        return limit
