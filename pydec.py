'''
   The License:
   
   Asterix-dz is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
 
   Asterix-dz is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
 
   You should have received a copy of the GNU General Public License
   along with Asterix-dz.  If not, see <http://www.gnu.org/licenses/>.

   Q29kZWQgQnkgIk9TZHogRHpheWVyIgpXaXRoIHRoZSBoZWxwIE9mIFJhb3VmCkZhY2Vib29rOiBPU2RldmR6Cg==

'''

import sys, getopt 
airline_code = [['JOR', '  Blue Air (Romania) Blue Transport\n'], ['AMB', '  Deutsche Rettungsflugwacht (Germany) Civil Air Ambulance\n'], ['EJA', '  Netjets (USA) Execjet\n'], ['DBB', '  Deutsche Bahn (Germany)\n'], ['TGV', '  SNCF (France)\n'], ['DYA', '  Dynamic Airways/Dynamic International Airways (USA) Dynamic Air\n'], ['AGU', '  Angara Airlines (Russia) Sarma\n'], ['SRU', '  Star Peru (Peru) Star Up\n'], ['VBW', '  Air Burkina (Burkina Faso) Burkina\n'], ['GLG', '  Aerogal Aerolineas Galapagos (Ecuador) Aerogal\n'], ['BOL', '  Transportes Aereos Bolivianos (Bolivia) Bol\n'], ['OAW', '  Helvetic Airways (Switzerland) Helvetic\n'], ['NTJ', '  Nextjet (Sweden) Nextjet\n'], ['GAP', '  PAL Express (Philippines) Airphil\n'], ['SNC', '  Air Cargo Carriers (USA) Night Cargo\n'], ['CMV', '  Calima Aviacion (Spain) Calima\n'], ['GSB', '  Gading Sari Aviation Services (Malaysia) Gading Sari\n'], ['AIE', '  Air Inuit (Canada) Air Inuit\n'], ['JBW', '  Jubba Airways (Kenya) Airjub\n'], ['JSA', '  Jetstar Asia Airways (Singapore) Jetstar Asia\n'], ['ISK', '  Intersky (Austria) Intersky\n'], ['SIL', '  Silver Airways (USA) Silver Wings\n'], ['URG', '  Air Urga (Ukraine) Urga\n'], ['MAC', '  Air Arabia Maroc (Morocco) Nawras\n'], ['TNM', '  Tiara Air (Aruba) Tiara\n'], ['RGR', '  Avior Regional (Venezuela) Avior RegionalGromov Airline\n'], ['BOX', '  AeroLogic (Germany) German Cargo\n'], ['GUY', '  Air Guyane Express/Air Antilles Express (French Guiana) Green Bird\n'], ['TRQ', '  Tarco Airlines (Sudan) Airtarco\n'], ['CSC', '  Sichuan Airlines (China) Si Chuan\n'], ['TAY', '  TNT Airways (Belgium) Quality\n'], ['MWI', '  Malawian Airlines (Malawi)\n'], ['XBO', '  Baseops International (USA)\n'], ['TVP', '  Travel Service Polska (Poland) Jettravel\n'], ['AKL', '  Air Kiribati (Kiribati)\n'], ['TUP', '  Aviastar-TU (Russia) Tupolevair\n'], ['BTQ', '  Boutique Air (Canada) Boutique\n'], ['ARE', '  LAN Colombia (Colombia) Aires\n'], ['ASD', '  Air Sinai (Egypt) Air Sinai\n'], ['SBO', '  Stabo Air (Zambia) Stabair\n'], ['GZP', '  Gazpromavia (Russia) Gazprom\n'], ['UBD', '  United Airways (Bangladesh) United Bangladesh\n'], ['IZM', '  Izair (Turkey) Izmir\n'], ['FDK', '  FlyDamas (Syria) Damavia\n'], ['KBA', '  Kenn Borek Air (Canada) Borek Air\n'], ['DSM', '  LAN Argentina (Argentina) Lan Ar\n'], ['ANT', '  Air North Charter (Canada) Air North\n'], ['AIJ', '  Interjet/ABC Aerolineas (Mexico) ABC Aerolineas\n'], ['SFW', '  Safi Airways (United Arab Emirates) Safi Airways\n'], ['OLC', '  Solar Cargo (Venezuela) Solarcargo\n'], ['BHP', '  Belair Airlines (Switzerland) Belair\n'], ['GWI', '  Germanwings (Germany) Germanwings\n'], ['AJK', '  Allied Air Cargo (Nigeria) Bambi\n'], ['WAV', '  Warbelow\xe2\x80\x99s Air Ventures (USA) Warbelow\n'], ['MEC', '  Air Mercury/Mercury Air Cargo (USA) Mercair\n'], ['TUD', '  Flight Alaska/Yute Air (USA) Tundra\n'], ['LNK', '  SA Airlink/Airlink (South Africa) Link\n'], ['AIP', '  Alpine Air Express (USA) Alpine Air\n'], ['BSX', '  Bassaka Air (Cambodia) Bassaka\n'], ['ICL', '  CAL Cargo Air Lines/Cavei Avir Levitanim (Israel) Cal\n'], ['NRR', '  Nature Air (Costa Rica) Nature Air\n'], ['SLI', '  Aeromexico Connect (Mexico) Costera\n'], ['FFV', '  Fly540/Five Forty Aviation (Kenya) Swift Tango\n'], ['CEB', '  Cebu Pacific Air (Philippines) Cebu Air\n'], ['HFY', '  Hifly (Portugal) Sky Flyer\n'], ['MNT', '  FlyMontserrat/Montserrat Airways (Montserrat) Montserrat\n'], ['AUL', '  Nordavia (Russia) Archangelsk Air\n'], ['FPO', '  Europe Airpost (France) French Post\n'], ['BVR', '  ACM Air Charter (Germany) Bavarian\n'], ['RUC', '  Rutas Aereas CA/RUTACA Airlines (Venezuela) Rutaca\n'], ['GAK', '  Global Aviation and Services Group (Libya) Aviagroup\n'], ['PSV', '  Servicios Aereos Profesionales (Dominican Rep.) Proservicios\n'], ['MPE', '  Canadian North (Canada) Empress\n'], ['TGU', '  Transportes Aereos Guatemaltecos (Guatemala) Chapin\n'], ['VTS', '  Everts Air/Tatonduk Outfitters (USA) Everts\n'], ['UPS', '  UPS Airlines/United Parcel Service (USA) UPS\n'], ['GTI', '  Atlas Air (USA) Giant\n'], ['KEM', '  CemAir (South Africa) CemAir\n'], ['BLX', '  TUIfly Nordic (Sweden) Bluescan\n'], ['PAS', '  Pelita Air Service (Indonesia) Pelita\n'], ['IGO', '  IndiGo Airlines (India) Ifly\n'], ['FAO', '  Falcon Air Express (USA) Panther\n'], ['FRJ', '  Afrijet Airlines (Nigeria) Afrijet\n'], ['RLX', '  Go2Sky (Slovakia) Relax\n'], ['ISR', '  Israir (Israel) Israir\n'], ['IBZ', '  International Business Air (Sweden) Interbiz\n'], ['MMD', '  Alsie Express/MMD (Denmark) Mermaid\n'], ['VVA', '  Aviast (Russia) Ialsi\n'], ['SNJ', '  Skynet Asia Airways (Japan) Newsky\n'], ['AKK', '  Aklak Air (Canada) Aklak\n'], ['DRU', '  Alrosa Mirny Air Enterprise (Russia) Mirny\n'], ['TNO', '  Aerounion/Aerotransporte de Carga Union (Mexico) Aero Union\n'], ['LMT', '  Almaty Aviation (Kazakhstan) Almaty\n'], ['SOV', '  Saravia Saratov Airlines (Russia) Saratov Air\n'], ['LTC', '  SmartLynx Airlines (Latvia) Latcharter\n'], ['COY', '  Coyne Airways (United Kingdom) Coyne Air\n'], ['JJA', '  Jeju Air (Korea \xe2\x80\x93 Rep. of) Jeju Air\n'], ['AWU', '  Sylt Air (Germany) Sylt-Air\n'], ['FAB', '  First Air (Canada) First Air\n'], ['SFJ', '  StarFlyer (Japan) Starflyer\n'], ['CAI', '  Corendon Airlines (Turkey) Corendon\n'], ['ERH', '  ERA Aviation (USA) Erah\n'], ['CSV', '  Coastal Travel Limited (Tanzania) Coastal Travel\n'], ['INC', '  Insel Air (Curacao) Inselair\n'], ['TJK', '  Tajik Air (Tajikistan) Tajik Air\n'], ['KGL', '  Metrojet/Kolavia/Kogalymavia Airlines (Russia) Kogalym\n'], ['CRN', '  Aero Caribbean (Cuba) Aerocaribbean\n'], ['AAG', '  Air Atlantique (United Kingdom) Atlantic\n'], ['TLR', '  Air Libya (Libya) Air Libya\n'], ['RYA', '  Arctic Transportation Services/Ryan Air Services (USA) Ryan Air\n'], ['AGV', '  Air Glaciers (Switzerland) Air Glaciers\n'], ['RTM', '  Aero Express Del Ecuador (Ecuador) Aero Transam\n'], ['TOB', '  Tobruk Air Transport and Cargo (Libya) Tobruk Air\n'], ['WRC', '  Wind Rose Aviation (Ukraine) Windrose\n'], ['AGO', '  Angola Air Charter (Angola) Angola Charter\n'], ['NYL', '  Mid Airlines (Sudan) Nile\n'], ['ATN', '  Air Transport International ATI (USA) Air Transport\n'], ['EXV', '  Expo Aviation (Sri Lanka) Expo Avia\n'], ['BRG', '  Bering Air (USA) Bering Air\n'], ['STP', '  STP Airways (Sao Tome and Principe) Saotome Airways\n'], ['BGH', '  BH Air (Bulgaria) Balkan Holidays\n'], ['LKE', '  Lucky Air (China) Lucky Air\n'], ['RHC', '  Redhill Aviation (United Kingdom) Redair\n'], ['MMA', '  Myanmar Airways International (Myanmar) Myanmar\n'], ['NKF', '  Barents AirLink/Nordkalottflyg (Sweden) Nordflight\n'], ['PCO', '  Pacific Coastal Airlines (Canada) Pasco\n'], ['BAJ', '  Baker Aviation (USA) Baker Aviation\n'], ['OHY', '  Onur Air (Turkey) Onur Air\n'], ['OLS', '  Sol Lineas Aereas (Argentina) Flight Sol\n'], ['AAW', '  Afriqiyah Airways (Libya) Afriqiyah\n'], ['ACP', '  Astral Aviation (Kenya) Astral Cargo\n'], ['PWF', '  Private Wings Flugcharter (Germany) Private Wings\n'], ['CYZ', '  China Postal Airlines (China) China Post\n'], ['GGE', '  EGA Ecuato Guineana de Aviacion (Equatorial Guinea) Ecuato Guineana\n'], ['EZX', '  Eaglexpress (Malaysia) Eaglexpress Air\n'], ['WDA', '  Wimbi Dira Airways (Congo \xe2\x80\x93 Democratic Rep.) Wimbi Dira\n'], ['THE', '  Toumai Air Tchad (Chad) Toumai Air\n'], ['FLG', '  Endeavor Air (USA) Flagship\n'], ['PGP', '  Perm Airlines (Russia) Perm Air\n'], ['CGN', '  Changan Airlines (China) Changan\n'], ['DAN', '  Dana Air (Nigeria) Danaco\n'], ['KAP', '  Cape Air (USA) Cair\n'], ['GLR', '  Central Mountain Air (Canada) Glacier\n'], ['NSE', '  SATENA (Colombia) Satena\n'], ['VAP', '  Phuket Air (Thailand) Phuket Air\n'], ['CQH', '  Spring Airlines (China) Air Spring\n'], ['SOO', '  Southern Air (USA) Southern Air\n'], ['ABS', '  Transwest Air (Canada) Athabaska\n'], ['RUN', '  ACT Airlines (Turkey) Cargo Turk\n'], ['MLD', '  Air Moldova (Moldova) Air Moldova\n'], ['AMV', '  AMC Airlines (Egypt)\n'], ['ROI', '  Avior Airlines (Venezuela) Avior\n'], ['JAI', '  Jet Airways (India) Jet Airways\n'], ['AXY', '  New Axis Airways (France) Axis\n'], ['CIU', '  Cielos Airlines (Peru) Cielos\n'], ['AEE', '  Aegean Airlines (Greece) Aegean\n'], ['HOP', '  Hop! (France) Air Op\n'], ['BGL', '  Benin Golf Air (Benin) Benin Golf\n'], ['TGZ', '  Georgian Airways/Air Zena (Georgia) Tamazi\n'], ['AAL', '  American Airlines (USA) American\n'], ['BER', '  Air Berlin (Germany) Air Berlin\n'], ['ACA', '  Air Canada (Canada) Air Canada\n'], ['AZU', '  Azul Linhas Aereas Brasileiras (Brazil) Azul\n'], ['MDA', '  Mandarin Airlines (Taiwan) Mandarin\n'], ['AFR', '  Air France (France) Airfrans\n'], ['ABR', '  Air Contractors (Ireland) Contract\n'], ['DAH', '  Air Algerie (Algeria) Air Algerie\n'], ['AIA', '  Airmark Indonesia (Indonesia) Airmark\n'], ['AIC', '  Air India (India) Air India\n'], ['NIG', '  Aero Contractors (Nigeria) Aeroline\n'], ['AXM', '  AirAsia (Malaysia) Red Cap\n'], ['TXC', '  Transaviaexport Cargo Airline (Belarus) Transexport\n'], ['AMX', '  Aeromexico (Mexico) Aeromexico\n'], ['ARG', '  Aerolineas Argentinas (Argentina) Argentina\n'], ['ASA', '  Alaska Airlines (USA) Alaska\n'], ['RAM', '  Royal Air Maroc (Morocco) Royalair Maroc\n'], ['AUT', '  Austral Lineas Aereas (Argentina) Austral\n'], ['AVA', '  Avianca (Colombia) Avianca\n'], ['AWN', '  Air Niamey (Niger) Air Niamey\n'], ['SCH', '  CHC Airways (Netherlands) Schreiner\n'], ['LOF', '  Trans States Airlines (USA) Waterski\n'], ['FIN', '  Finnair (Finland) Finnair\n'], ['AZA', '  Alitalia (Italy) Alitalia\n'], ['BRU', '  Belavia (Belarus) Belarus Avia\n'], ['BCF', '  BACH Flugbetriebs (Austria) Bach\n'], ['BKA', '  Bankair (USA) Bankair\n'], ['EXZ', '  East African Safari Air Express (Kenya) Twiga\n'], ['JBU', '  JetBlue Airways {Jet Blue} (USA) Jetblue\n'], ['UIA', '  UNI Airways Corporation (Taiwan) Glory\n'], ['ERT', '  Eritrean Airlines (Eritrea) Eritrean\n'], ['IRB', '  Iran Air Tours (Iran)\n'], ['BAT', '  British Airways (BA) Limited (United Kingdom) Gherkin \xe2\x80\x93 LCY-JFK flights only\n'], ['BAW', '  British Airways Plc (United Kingdom) Speedbird\n'], ['SHT', '  British Airways Shuttle (United Kingdom) Shuttle\n'], ['SBS', '  Seaborne Airlines (Virgin Islands \xe2\x80\x93 USA) Seaborne\n'], ['SKY', '  Skymark Airlines (Japan) Skymark\n'], ['BEE', '  flybe (United Kingdom) Jersey\n'], ['FCM', '  flybe Nordic/Finnish Commuter Airlines (Finland) Finncomm\n'], ['BBD', '  Bluebird Cargo (Iceland) Blue Cargo\n'], ['RSR', '  Aero-Service (Congo) Congoserv\n'], ['BBC', '  Biman Bangladesh (Bangladesh) Bangladesh\n'], ['BHA', '  Hawkair (Canada) Hawk\n'], ['RBA', '  Royal Brunei Airlines (Brunei Darussalam) Brunei\n'], ['BRJ', '  Borajet (Turkey) Bora Jet\n'], ['LBT', '  Nouvelair (Tunisia) Nouvelair\n'], ['OKA', '  Okay Airways (China) Okayjet\n'], ['PIC', '  Jetstar Pacific Airlines (Vietnam) Pacific\n'], ['BMR', '  bmi Regional (United Kingdom) Kittiwake\n'], ['BBW', '  BB Airways (Nepal)\n'], ['BOT', '  Air Botswana (Botswana) Botswana\n'], ['BBV', '  Bravo Airlines (Spain) Bravo Europa\n'], ['EVA', '  EVA Airways Corporation (Taiwan) Eva\n'], ['BIH', '  British International Helicopters (United Kingdom) Brintel\n'], ['BTI', '  Air Baltic (Latvia) Air Baltic\n'], ['BPA', '  Blue Panorama Airlines/Blu-Express (Italy) Blue Panorama\n'], ['BWA', '  Caribbean Airlines/Air Jamaica (Trinidad and Tobago) Caribbean Airlines\n'], ['ABL', '  Air Busan (Korea \xe2\x80\x93 Rep. of) Air Busan\n'], ['TOM', '  Thomson Airways (United Kingdom) Tomson\n'], ['BBG', '  Bluebird Airways (Greece) Candia Bird\n'], ['BDA', '  Blue Dart Aviation (India) Blue Dart\n'], ['KEE', '  Keystone Air Service (Canada) Keystone\n'], ['CEL', '  CEIBA Intercontinental (Equatorial Guinea) Ceiba Line\n'], ['IMX', '  Zimex Aviation (Switzerland) Zimex\n'], ['UCA', '  Commutair (USA) Commutair\n'], ['CJA', '  CanJet (Canada) Canjet\n'], ['CIN', '  Cinnamon Air (Sri Lanka) Cinnamon\n'], ['CAO', '  Air China Cargo (China) Airchina Freight\n'], ['CCA', '  Air China (China) Air China\n'], ['CCD', '  Dalian Airlines (China) Xiangjian\n'], ['ABD', '  Air Atlanta Icelandic (Iceland) Atlanta\n'], ['LLR', '  Air India Regional (India) Allied\n'], ['TOK', '  Airlines PNG/Airlines of Papua New Guinea (Papua New Guinea) Balus\n'], ['BMJ', '  Bemidji Airlines (USA) Bemidji\n'], ['CAL', '  China Airlines (Taiwan) Dynasty\n'], ['CFE', '  BA CityFlyer Express (United Kingdom) Flyer\n'], ['CKK', '  China Cargo Airlines (China) Cargo King\n'], ['CLH', '  Lufthansa Cityline (Germany) Hansa Line\n'], ['CLW', '  LOT Charters (Poland) Central Wings\n'], ['CMP', '  Copa Airlines (Panama) Copa\n'], ['GDC', '  Grand China Air (China) Grand China\n'], ['CPZ', '  Compass Airlines (USA) Compass Rose\n'], ['EXL', '  Sunshine Express Airlines (Australia)\n'], ['CYL', '  Alitalia CityLiner (Italy) Cityliner\n'], ['CUB', '  Cubana de Aviacion (Cuba) Cubana\n'], ['CLX', '  Cargolux (Luxembourg) Cargolux\n'], ['CVA', '  Air Chathams (New Zealand) Chatham\n'], ['MRS', '  Air Marshall Islands (Marshall Islands) Marshall Islands\n'], ['CPA', '  Cathay Pacific Airways (Hong Kong) Cathay\n'], ['CYP', '  Cyprus Airways (Cyprus) Cyprus\n'], ['CSN', '  China Southern Airlines (China) China Southern\n'], ['DHK', '  DHL Air UK/DHL Air Ltd (United Kingdom) Eurotrans\n'], ['SSF', '  Severstal Aircompany (Russia) Severstal\n'], ['DAO', '  Daallo Airlines (Djibouti) Dalo Airlines\n'], ['LID', '  Alidaunia (Italy) Alida\n'], ['DAE', '  DHL Aero Expreso (Panama) Yellow\n'], ['ILN', '  Inter Air (South Africa) Inline\n'], ['XAX', '  AirAsia X (Malaysia) Xanadu\n'], ['DNV', '  Donavia (Russia) Donavia\n'], ['GAO', '  Golden Air (Sweden) Golden\n'], ['NOK', '  Nok Air (Thailand) Nok Air\n'], ['CFG', '  Condor Airlines (Germany) Condor\n'], ['DER', '  Beijing Capital Airlines (China) Deer Jet\n'], ['SRQ', '  South East Asian Airlines (Philippines) Seair\n'], ['VOZ', '  Virgin Australia Airlines (Australia) Virgin\n'], ['PBN', '  Virgin Samoa (Samoa) Bluebird\n'], ['VKG', '  Thomas Cook Airlines Scandinavia (Denmark) Viking\n'], ['DAL', '  Delta Air Lines (USA) Delta\n'], ['SGG', '  Senegal Airlines (USA) Senegal Air\n'], ['CXT', '  Coastal Air Transport (USA) Coastal\n'], ['EZS', '  easyJet Switzerland (Switzerland) Top Swiss\n'], ['DTA', '  TAAG Angola Airlines (Angola) DTA\n'], ['NLH', '  Norwegian Long Haul (Norway) Norstar\n'], ['VSV', '  Scat Air/PLL Scat Aircompany (Kazakhstan) Vlasta\n'], ['UCR', '  Aero Charter Ukraine (Ukraine) Charter Ukraine\n'], ['DTR', '  DAT Danish Air Transport (Denmark) Danish\n'], ['NAX', '  Norwegian Air Shuttle (Norway) Nor Shuttle\n'], ['RBG', '  Air Arabia Egypt (Egypt) Arabia Egypt\n'], ['ESF', '  Estafeta Carga Aerea (Mexico) Estafeta\n'], ['GTA', '  City Airways (Thailand) City Airways\n'], ['EVE', '  Evelop Airlines (Spain) Evelop\n'], ['PLM', '  Pullmantur Air (Spain) Pullmantur\n'], ['BOS', '  OpenSkies (United Kingdom) Mistral\n'], ['TWN', '  Avialeasing Aviation Company (Uzbekistan) Twin Arrow\n'], ['ABQ', '  Airblue (Pakistan) Airblue\n'], ['ESY', '  EasyFly (Colombia) Easy Fly\n'], ['ENJ', '  Enerjet (Canada) Enerjet Air\n'], ['AKX', '  ANA Wings (Japan) Alfa Wing\n'], ['EIN', '  Aer Lingus (Ireland) Shamrock\n'], ['NEA', '  New England Airlines (USA) New England\n'], ['UAE', '  Emirates (United Arab Emirates) Emirates\n'], ['AEB', '  Aero Benin (Benin) Aeroben\n'], ['CFS', '  Empire Airlines (USA) Empire Air\n'], ['DLA', '  Air Dolomiti (Italy) Dolomiti\n'], ['LHN', '  Express One International (USA) Longhorn\n'], ['IRC', '  Iran Asseman Airlines (Iran)\n'], ['TAE', '  TAME (Ecuador) Tame\n'], ['DHX', '  SNAS/DHL/DHL International Aviation ME (Bahrain) Dilmun\n'], ['ETH', '  Ethiopian Airlines (Ethiopia) Ethiopian\n'], ['UEA', '  Chengdu Airlines (China) Hibiscus City\n'], ['ASQ', '  ExpressJet Airlines (USA) Acey\n'], ['EWG', '  Eurowings (Germany) Eurowings\n'], ['BJK', '  Atlantic Airlines (USA) Blackjack\n'], ['EFL', '  Eagle Air (Tanzania) Flying Eagle\n'], ['ETD', '  Etihad Airways (United Arab Emirates) Etihad\n'], ['EIA', '  Evergreen International Airlines (USA) Evergreen\n'], ['SUS', '  Sun Air of Scandinavia (Denmark) Sun Scan\n'], ['FSW', '  Faso Airways (Burkina Faso) Faso\n'], ['FXL', '  Fly Excellent (Sweden) Fly Excellent\n'], ['SGB', '  Sky King (USA) Songbird\n'], ['DWT', '  Darwin Airline/Etihad Regional (Switzerland) Darwin\n'], ['VRE', '  Volare Airlines (Ukraine) Ukraine Volare\n'], ['FFT', '  Frontier Airlines (USA) Frontier Flight\n'], ['SFR', '  Safair/FlySafair (South Africa)\n'], ['LZB', '  Bulgaria Air (Bulgaria) Flying Bulgaria\n'], ['FCX', '  Falcon Express Cargo Airlines (United Arab Emirates) Falcon Cargo\n'], ['AIQ', '  Thai AirAsia (Thailand) Thai Asia\n'], ['AFG', '  Ariana Afghan Airlines (Afghanistan) Ariana\n'], ['ICE', '  Icelandair (Iceland) Ice Air\n'], ['FJI', '  Fiji Airways (Fiji) Fiji\n'], ['FJA', '  Pacific Sun/Fiji Airlines  Pac Sun\n'], ['WTA', '  Africa West Airlines (Togo) West Togo\n'], ['CSH', '  Shanghai Airlines (China) Shanghai Air\n'], ['FTZ', '  Fastjet (United Kingdom/Tanzania) Greybird\n'], ['RGL', '  Royal Air Maroc Express/Regional Airlines (Morocco) Maroc Regional\n'], ['ATM', '  Airlines of Tasmania (Australia) Air Tas\n'], ['FXX', '  Felix Airways (Yemen)\n'], ['FPG', '  TAG Aviation (Switzerland) Tag Aviation\n'], ['FRE', '  Freedom Air/Aviation Services (Guam) Freedom\n'], ['TCW', '  Thomas Cook Airlines Belgium (Belgium) Thomas Cook\n'], ['RYR', '  Ryanair (Ireland) Ryanair\n'], ['SYA', '  Syphax Airlines (Tunisia) Syphaxair\n'], ['SDM', '  Rossiya Russian Airlines (Russia) Russia\n'], ['FRI', '  Ibex Airlines (Japan) Ibex\n'], ['FDX', '  FedEx Express/Federal Express (USA) Fedex\n'], ['FFM', '  Firefly (Malaysia) Firefly\n'], ['NWR', '  Northwest Regional Airlines (Australia)\n'], ['FDB', '  Flydubai (United Arab Emirates) Sky Dubai\n'], ['VXG', '  Avirex Gabon (Gabon) Avirex Gabon\n'], ['GLO', '  GOL Transportes Aereos (Brazil) Gol Transporte\n'], ['AAY', '  Allegiant Air (USA) Allegiant\n'], ['GZD', '  Grizodubova Air Company (Russia) Grizodubova Air\n'], ['HXA', '  China Express Airlines (China) China Express\n'], ['GJS', '  GoJet Airlines (USA) Lindbergh\n'], ['ENK', '  Enkor (Russia) Enkor\n'], ['GOW', '  GoAir (India) Go Air\n'], ['ABY', '  Air Arabia (United Arab Emirates) Arabia\n'], ['GIA', '  Garuda Indonesia (Indonesia) Indonesia\n'], ['ABX', '  ABX Air (USA) Abex\n'], ['GCB', '  Lina Congo (Congo) Linacongo\n'], ['GNR', '  Gambia International Airlines (Gambia) Gambia International\n'], ['TNA', '  TransAsia Airways (Taiwan) Trans Asia\n'], ['GFA', '  Gulf Air (Bahrain) Gulf Air\n'], ['GLP', '  Globus (Russia) Globus\n'], ['CDC', '  Zhejiang Loong Airlines (China) Gualong\n'], ['JJP', '  JetStar Japan (Japan) Orange Liner\n'], ['GRL', '  Air Greenland (Denmark) Greenlandair\n'], ['KZU', '  ULS Airlines Cargo Transport (Turkey) Universal Cargo\n'], ['GDR', '  Gadair European Airlines (Spain) Gadair Lines\n'], ['GES', '  Gestair (Spain) Gestair\n'], ['SEH', '  Sky Express (Greece) Air Crete\n'], ['AUR', '  Aurigny Air Services (United Kingdom) Ayline\n'], ['GCR', '  Tianjin Airlines (China) China Dragon\n'], ['JXX', '  Primera Air (Iceland) Jetbird\n'], ['GBK', '  Gabon Airlines (Gabon) Gabon Airlines\n'], ['TMG', '  Tri-MG Intra Asia Airlines (Indonesia) Trilines\n'], ['SKU', '  Sky Airline (Chile) Aerosky\n'], ['HRM', '  Hermes Airlines (Greece) Hermes\n'], ['HLI', '  Heli Securite Helicopter Airlines (France) Heli Saint Tropez\n'], ['RSY', '  I-Fly (Russia) Russian Sky\n'], ['BUC', '  Bulgarian Air Charter (Bulgaria) Bulgarian Charter\n'], ['HAG', '  Hageland Aviation Services (USA) Hageland\n'], ['EGU', '  Eagle Air (Uganda) African Eagle\n'], ['HTH', '  Helitt Lineas Aereas (Spain) Alboran\n'], ['HAL', '  Hawaiian Airlines (USA) Hawaiian\n'], ['AAQ', '  Asia Atlantic Airlines (Thailand) Asia Atlantic\n'], ['ADO', '  Hokkaido International Airlines/Air Do (Japan) Air Do\n'], ['LGW', '  LGW Luftfahrtgesellschaft Walter (Germany) Walter\n'], ['VRE', '  Air C\xc3\xb4te d\xe2\x80\x99Ivoire (Cote d\xe2\x80\x99Ivoire) Cote d\xe2\x80\x99Ivoire\n'], ['NLY', '  Niki (Austria) Flyniki\n'], ['TMN', '  Tasman Cargo Airlines (Australia) Tasman\n'], ['FSC', '  Four Star Air Cargo (Virgin Islands \xe2\x80\x93 USA) Four Star\n'], ['HAY', '  Hamburg Airways (Germany) Hamburg Airways\n'], ['SEY', '  Air Seychelles (Seychelles) Seychelles\n'], ['HVY', '  HeavyLift Cargo Airlines (Australia) Heavy Cargo\n'], ['PTH', '  Proteus Helicopteres (France) Proteus\n'], ['DKH', '  Juneyao Airlines (China) Air Juneyao\n'], ['HHN', '  Hahn Air (Germany) Rooster\n'], ['HSV', '  Svenska Direktflyg (Sweden) Highswede\n'], ['IMP', '  Hellenic Imperial Airways (Greece) Imperial\n'], ['CHH', '  Hainan Airlines (China) Hainan\n'], ['TRA', '  transavia.com/Transavia Airlines (Netherlands) Transavia\n'], ['NWL', '  North-Wright Airways (Canada) Northwright\n'], ['CRK', '  Hong Kong Airlines (Hong Kong) Bauhinia\n'], ['UZB', '  Uzbekistan Airways (Uzbekistan) Uzbek\n'], ['SHU', '  Aurora (Russia) Satair\n'], ['IBS', '  Iberia Express (Spain) Iberexpres\n'], ['FWA', '  Interstate Airlines (Netherlands) Freewayair\n'], ['IAD', '  AirAsia India (India) Ariya\n'], ['CMM', '  Air Mali (Mali) Camali\n'], ['SEQ', '  Sky Eyes (Thailand) Sky Eyes\n'], ['IAW', '  Iraqi Airways (Iraq) Iraqi\n'], ['IBE', '  Iberia (Spain) Iberia\n'], ['BTK', '  Batik Air (Indonesia) Batik\n'], ['SOL', '  Solomon Airlines (Solomon Islands) Solomon\n'], ['ISS', '  Meridiana Fly (Italy) Merair\n'], ['MZA', '  Irtysh Air (Kazakhstan) Azamat\n'], ['CSQ', '  IBC Airways (USA) Chasqui\n'], ['MNJ', '  Menajet (Lebanon) Menajet\n'], ['IRA', '  Iran Air (Iran) Iran Air\n'], ['ISA', '  Island Airlines (USA) Island\n'], ['WON', '  Wings Abadi Air (Indonesia) Wings Abadi\n'], ['AXB', '  Air India Express (India) Express India\n'], ['IYE', '  Yemenia (Yemen) Yemeni\n'], ['AIZ', '  Arkia (Israel) Arkia\n'], ['AHC', '  AZAL Avia Cargo (Azerbaijan) Azalaviacargo\n'], ['AHY', '  AZAL Azerbaijan Airlines/AHY (Azerbaijan) Azal\n'], ['PLR', '  Northwestern Air (Canada) Polaris\n'], ['BFL', '  Buffalo Airways (Canada) Buffalo Airways\n'], ['EPA', '  Shenzhen Donghai Airlines (China) Donghai Air\n'], ['ARW', '  Jamaica Air Shuttle (Jamaica) Jamaica Shuttle\n'], ['DNM', '  Denim Air (Netherlands) Denim\n'], ['BVT', '  Berjaya Air (Malaysia) Berjaya\n'], ['JZR', '  Jazeera Airways (Kuwait) Jazeera\n'], ['BON', '  B & H Airlines (Bosnia-Herzegovina) BH Airlines\n'], ['JGN', '  Jagson Airlines (India)\n'], ['JBA', '  Helijet International (Canada) Helijet\n'], ['JEX', '  JAL Express (Japan) Janex\n'], ['JAC', '  Japan Air Commuter (Japan) Commuter\n'], ['MNO', '  Mango (South Africa) Tulca\n'], ['LAB', '  LAB Flying Service (USA) Lab\n'], ['FDA', '  Fuji Dream Airlines (Japan) Fuji Dream\n'], ['AGX', '  Aviogenex (Serbia) Genex\n'], ['TAM', '  TAM Linhas Aereas (Brazil) Tam\n'], ['JAL', '  Japan Airlines (Japan) Japan Air\n'], ['JKT', '  Jetstar Hong Kong (Italy) Kai Tak\n'], ['NLV', '  Livingston Compagnia Aerea (Italy) Seagull\n'], ['ADR', '  Adria Airways (Slovenia) Adria\n'], ['JST', '  Jetstar Airways (Australia) Jetstar\n'], ['LAV', '  AlbaStar (Spain) Alba Star\n'], ['JOY', '  Joy Air (China) Joy Air\n'], ['KOR', '  Air Koryo (Korea \xe2\x80\x93 Dem. People\xe2\x80\x99s Rep.) Air Koryo\n'], ['LNI', '  Lion Airlines/Lion Mentari Air (Indonesia) Lion Inter\n'], ['JAT', '  Jat Airways (Serbia) Jat\n'], ['BLS', '  Bearskin Airlines (Canada) Bearskin\n'], ['VNL', '  Vanilla Air (Japan) Vanilla\n'], ['IWY', '  Air Turks and Caicos (Turks and Caicos Islands) Islandways\n'], ['ELO', '  EuroLOT (Poland) Eurolot\n'], ['CKS', '  Kalitta Air (USA) Connie\n'], ['ABE', '  Aban Air (Iran) Aban\n'], ['SQH', '  Wings of Alaska/SeaPort Airlines (USA) Sasquach\n'], ['KHV', '  Cambodia Angkor Air (Cambodia) Cambodia Air\n'], ['ZAK', '  Zambia Skyways (Zambia) Zambia Skies\n'], ['ESD', '  Esen Air (Kyrgyzstan) Esen Air\n'], ['KFS', '  Kalitta Charters (USA) Kalitta\n'], ['KRI', '  Krylo Aviakompania (Russia) Krilo\n'], ['HDA', '  Dragonair/Hong Kong Dragon Airlines (Hong Kong) Dragon\n'], ['DRK', '  Druk Air (Bhutan) Royal Bhutan\n'], ['KZR', '  Air Astana (Kazakhstan) Astana Line\n'], ['KAL', '  Korean Air (Korea \xe2\x80\x93 Rep. of) Korean Air\n'], ['BLF', '  Blue1 (Finland) Bluefin\n'], ['GTV', '  Aerogaviota (Cuba) Gaviota\n'], ['AAH', '  Aloha Air Cargo (USA) Aloha\n'], ['KKK', '  AtlasJet (Turkey) Atlasjet\n'], ['KLM', '  KLM Royal Dutch Airlines (Netherlands) KLM\n'], ['AMC', '  Air Malta (Malta) Air Malta\n'], ['CUA', '  China United Airlines (China) Lianhang\n'], ['AER', '  Alaska Central Express (USA) Ace Air\n'], ['QNK', '  Kabo Air (Nigeria) Kabo\n'], ['KQA', '  Kenya Airways (Kenya) Kenya\n'], ['KMZ', '  Comores Aviation (Comoros)\n'], ['PEN', '  Penair/Peninsula Airways (USA) Peninsula\n'], ['KAC', '  Kuwait Airways (Kuwait) Kuwaiti\n'], ['KFA', '  Kelowna Flightcraft Air Charter (Canada) Flightcraft\n'], ['CAY', '  Cayman Airways (Cayman Islands) Cayman\n'], ['NCA', '  Nippon Cargo Airlines (Japan) Nippon Cargo\n'], ['LYC', '  Lynden Air Cargo (USA) Lynden\n'], ['JOS', '  DHL de Guatemala (Guatemala)\n'], ['LTR', '  Lufttransport (Norway) Lufttransport\n'], ['MAI', '  Mauritanian Airlines International (Mauritania)\n'], ['VNZ', '  TAM Air/Tbilaviamsheni (Georgia) Tbilavia\n'], ['LHS', '  Lugansk Airlines (Ukraine) Enterprise Luhansk\n'], ['LAN', '  LAN Airlines (Chile) Lan Chile\n'], ['LBR', '  Air Costa (India)\n'], ['LOG', '  Loganair (United Kingdom) Logan\n'], ['AHK', '  Air Hong Kong (Hong Kong) Air Hong Kong\n'], ['TUY', '  Linea Turistica Aerotuy (Venezuela) Aereotuy\n'], ['LGL', '  Luxair (Luxembourg) Luxair\n'], ['DLH', '  Lufthansa (Germany) Lufthansa\n'], ['GEC', '  Lufthansa Cargo (Germany) Lufthansa Cargo\n'], ['LIA', '  LIAT (Antigua and Barbuda) Liat\n'], ['JNA', '  Jin Air (Korea \xe2\x80\x93 Rep. of) Jin Air\n'], ['SLA', '  Sierra National Airlines (Sierra Leone) Selair\n'], ['BSK', '  Miami Air International (USA) Biscayne\n'], ['LAA', '  Lybian Arab Airlines (Libya) Libair\n'], ['LOT', '  LOT Polish Airlines (Poland) Pollot\n'], ['LPE', '  LAN Peru (Peru) Patagonia\n'], ['LAQ', '  Lebanese Air Transport (Lebanon) Lat\n'], ['LRC', '  Lacsa (Costa Rica) Lacsa\n'], ['EXS', '  Jet2.com (United Kingdom) Channex\n'], ['LTU', '  Air Lituanica (Lithuania) Lituanica\n'], ['LXP', '  Lan Express (Chile) Lan Ex\n'], ['NMI', '  Pacific Wings/GeorgiaSkies/New Mexico Airlines (USA) Tsunami\n'], ['SWR', '  Swiss International Air Lines (Switzerland) Swiss\n'], ['SWU', '  Swiss European Air Lines (Switzerland) Euroswiss\n'], ['ELY', '  El Al (Israel) El Al\n'], ['MNG', '  Aero Mongolia (Mongolia) Aero Mongolia\n'], ['MZS', '  Mahfooz Aviation (Gambia) Mahfooz\n'], ['NFA', '  Air Norway/North Flying (Denmark) North Flying\n'], ['TUS', '  ABSA Aerolinhas Brasileiras (Brazil) Turismo\n'], ['AJT', '  Amerijet International (USA) Amerijet\n'], ['MAA', '  MasAir (Mexico) Mas Carga\n'], ['MSL', '  Marsland Aviation (Sudan) Marsland Air\n'], ['MSI', '  Motor Sich Aviakompania (Ukraine) Motor Sich\n'], ['MNB', '  MNG Airlines (Turkey) Black Sea\n'], ['MSC', '  Air Cairo (Egypt)\n'], ['RCH', '  Air Mobility Command (USA) Reach\n'], ['MDG', '  Air Madagascar (Madagascar) Air Madagascar\n'], ['MEA', '  MEA Middle East Airlines Airliban (Lebanon) Cedar Jet\n'], ['CXA', '  Xiamen Airlines (China) Xiamen Air\n'], ['MIX', '  Midex Airlines (United Arab Emirates) Midexcargo\n'], ['MAS', '  Malaysia Airlines (Malaysia) Malaysian\n'], ['MWG', '  MASwings (Malaysia) Maswings\n'], ['SLK', '  SilkAir (Singapore) Silkair\n'], ['MLR', '  Mihin Lanka (Sri Lanka) Mihin Lanka\n'], ['MAU', '  Air Mauritius (Mauritius) Air Mauritius\n'], ['BIE', '  Air Mediterranee (France) Mediterrannee\n'], ['ETC', '  ATTICO African Transport Trading and Investment Co. (Sudan) Tranattico\n'], ['APJ', '  Peach Aviation (Japan) Air Peach\n'], ['CAW', '  kulula.com/Comair Commercial Airlines (South Africa) Commercial\n'], ['AUH', '  Abu Dhabi Amiri Flight (United Arab Emirates) Sultan\n'], ['CAV', '  Calm Air (Canada) Calm Air\n'], ['MPH', '  Martinair (Netherlands) Martinair\n'], ['ENY', '  Envoy Air/American Eagle (USA) Envoy\n'], ['MML', '  Hunnu Air (Mongolia) Trans Mongolia\n'], ['MSE', '  EgyptAir Express (Egypt) Egyptair Express\n'], ['MSR', '  EgyptAir (Egypt) Egyptair\n'], ['TCX', '  Thomas Cook Airlines (United Kingdom) Kestrel\n'], ['CES', '  China Eastern Airlines (China) China Eastern\n'], ['BUG', '  Mokulele Airlines (USA) Speedbuggy\n'], ['MYD', '  Maya Island Air (Belize) Myland\n'], ['MWA', '  Midwest Airlines (Egypt)\n'], ['QNK', '  Kabo Air (Nigeria) Kabo\n'], ['NWS', '  Nordwind Airlines (Russia) Nordland\n'], ['TNB', '  Trans Air Benin (Benin) Trans Benin\n'], ['MDM', '  Medavia (Malta) Medavia\n'], ['SGY', '  Skagway Air Service (USA) Skagway Air\n'], ['MUA', '  National Airlines (USA) Murray Air\n'], ['NVR', '  Novair/Nova Airlines (Sweden) Navigator\n'], ['NAC', '  Northern Air Cargo (USA) Yukon\n'], ['NJS', '  Cobham Aviation Services Australia (Australia) National Jet\n'], ['NMA', '  Nesma Airlines (Egypt) Nesma\n'], ['AVN', '  Air Vanuatu (Vanuatu) Air Van\n'], ['ANA', '  ANA All-Nippon Airways (Japan) All Nippon\n'], ['PGA', '  Portugalia (Portugal) Portugalia\n'], ['NGB', '  Nordic Global Airlines (Finland) Nordic Global\n'], ['NKS', '  Spirit Airlines (USA) Spirit Wings\n'], ['SAI', '  Shaheen Air International (Pakistan) Shaheen Air\n'], ['NZM', '  Mount Cook Airline (New Zealand) Mount Cook\n'], ['MOV', '  VIM Airlines (Russia) Mov Air\n'], ['NOS', '  Neos (Italy) Moonflower\n'], ['NIA', '  Nile Air (Egypt) Nile Bird\n'], ['SKP', '  Skytrans Airlines (Australia) Skytrans\n'], ['AJX', '  Air Japan (Japan) Air Japan\n'], ['HBH', '  Hebei Airlines (China) Hebei Air\n'], ['IBB', '  Binter Canarias (Spain) Binter\n'], ['JTA', '  Japan Transocean Air (Japan) Jai Ocean\n'], ['AMU', '  Air Macau (Macau) Air Macao\n'], ['FNA', '  Air Iceland/Flugfelag Islands (Iceland) Faxi\n'], ['ANZ', '  Air New Zealand (New Zealand) New Zealand\n'], ['AWK', '  Airwork (New Zealand) Airwork\n'], ['RLK', '  Air Nelson (New Zealand) Link\n'], ['JEA', '  OLT Jetair (Poland) Jeta\n'], ['ABV', '  Antrak Air (Ghana) Antrak\n'], ['ONE', '  Avianca Brazil (Brazil) Oceanair\n'], ['NOV', '  Nova Airline (Sudan) Novanile\n'], ['OAL', '  Olympic Air (Greece) Olympic\n'], ['BOV', '  Boliviana de Aviacion (Bolivia)\n'], ['OAV', '  Omni Aviacao e Tecnologia/PGA Express (Portugal) Omni\n'], ['MXD', '  Malindo Air (Malaysia) Malindo Express\n'], ['ENT', '  Enter Air (Poland) Enterair\n'], ['TML', '  Transports et Travaux Aeriens de Madagascar (Madagascar) Tam Airline\n'], ['FJM', '  Fly Jamaica Airways (Jamaica) Greenheart\n'], ['CSA', '  Czech Airlines (Czech Rep.) CSA Lines\n'], ['MGL', '  MIAT Mongolian Airlines (Mongolia) Mongol Air\n'], ['RON', '  Our Airline (Nauru)\n'], ['SKW', '  Skywest Airlines (USA) Skywest\n'], ['CQN', '  Chongqing Airlines (China) Chong Qing\n'], ['CRF', '  Krym (Ukraine) Crimea Air\n'], ['TFL', '  Arkefly (Netherlands) Arkefly\n'], ['AUA', '  Austrian Airlines (Austria) Austrian\n'], ['CTN', '  Croatia Airlines (Croatia) Croatia\n'], ['ELL', '  Estonian Air (Estonia) Estonian\n'], ['OVA', '  Melilla Airlines (Spain) Aeronova\n'], ['OEA', '  Orient Thai Airlines (Thailand) Orient Thai\n'], ['ANS', '  Andes Lineas Aereas (Argentina) Aeroandes\n'], ['OAE', '  Omni Air Express/Omni Air International (USA) Omni Express\n'], ['AAR', '  Asiana Airlines (Korea \xe2\x80\x93 Rep. of) Asiana\n'], ['PFZ', '  Proflight Commuter Services (Zambia) Proflight Zambia\n'], ['XAK', '  Airkenya Express (Kenya) Sunexpress\n'], ['PTB', '  Passaredo Transportes Aereos (Brazil) Passaredo\n'], ['NSO', '  Aerolineas Sosa (Honduras) Sosa\n'], ['RPB', '  Copa Airlines Colombia (Colombia) Aerorepublica\n'], ['MUI', '  Trans Air (USA) Maui\n'], ['ESL', '  Russian Sky Airlines (Russia) Raduga\n'], ['PTN', '  Pantanal Linhas Aereas Sul-Matogrossenses (Brazil) Pantanal\n'], ['PVN', '  Peruvian Airlines (Peru) Peruvian\n'], ['FCL', '  Florida Coastal Airlines (USA) Florida Coastal\n'], ['SPR', '  Provincial Airlines (Canada) Speedair\n'], ['PGT', '  Pegasus Airlines (Turkey) Sun Turk\n'], ['POE', '  Porter Airlines (Canada) Porter\n'], ['PEV', '  People\xe2\x80\x99s Viennaline/Altenrhein Luftfahrt (Austria) Peoples\n'], ['PNW', '  Palestinian Airlines (Palestinian Territory) Palestinian\n'], ['BKP', '  Bangkok Airways (Thailand) Bangkok Air\n'], ['PAO', '  Polynesian Airlines (Samoa) Polynesian\n'], ['SPM', '  Air Saint-Pierre (St. Pierre and Miquelon) Saint-Pierre\n'], ['PIA', '  Pakistan International Airlines (Pakistan) Pakistan\n'], ['TOS', '  Tropic Air (Belize) Tropiser\n'], ['CHB', '  China West Air (China) West China\n'], ['PAC', '  Polar Air Cargo (USA) Polar\n'], ['PJS', '  Jet Aviation Business Jets (Switzerland) Jet Aviation\n'], ['APG', '  Philippines AirAsia (Philippines) Cool Red\n'], ['TFK', '  Transafrik International (Sao Tome and Principe)\n'], ['PAL', '  Philippine Airlines (Philippines) Philippine\n'], ['AUI', '  Ukraine International Airlines (Ukraine) Ukraine International\n'], ['SWN', '  West Air Sweden (Sweden) Air Sweden\n'], ['PNR', '  PAN Air Lineas Aereas (Spain) Skyjet\n'], ['PRF', '  Precision Air Services (Tanzania) Precision Air\n'], ['ANG', '  Air Niugini (Papua New Guinea) Niugini\n'], ['SLM', '  Surinam Airways (Suriname) Surinam\n'], ['LAP', '  TAM Airlines/Transportes Aereos del Mercosur (Paraguay) Paraguaya\n'], ['DQA', '  Maldivian/Island Aviation Services (Maldives) Island Aviation\n'], ['MLA', '  40-Mile Air (USA) Mile Air\n'], ['CDP', '  Aero Condor (Peru) Condor Peru\n'], ['PEC', '  Pacific East Asia Cargo Airlines (Philippines) Cool Red\n'], ['TSG', '  Trans Air Congo (Congo) Trans Congo\n'], ['CIM', '  Cimber (Denmark) Cimber\n'], ['GFG', '  SkyGeorgia (Georgia) National\n'], ['QCL', '  Air Class Lineas Aereas (Uruguay) Acla\n'], ['EAQ', '  Eastern Australia Airlines (Australia) Eastern\n'], ['QFA', '  Qantas Airways (Australia) Qantas\n'], ['QLK', '  QantasLink (Australia) Q Link\n'], ['QNZ', '  JetConnect (New Zealand) Qantas JetConnect\n'], ['SSQ', '  Sunstate Airlines (Australia) Sunstate\n'], ['LYN', '  Kyrgyzstan (Kyrgyzstan) Altyn Avia\n'], ['JZA', '  Jazz Aviation/Air Canada Express (Canada) Jazz\n'], ['LER', '  LASER Linea Aerea de Servicio Ejecutivo Regional (Venezuela) Laser\n'], ['RNL', '  Aero Lanka/Serendib Express (Sri Lanka) Aero Lanka\n'], ['AML', '  Air Malawi (Malawi) Malawi\n'], ['ARR', '  Air Armenia (Armenia) Air Armenia\n'], ['UTY', '  Alliance Airlines (Australia) Unity\n'], ['QTR', '  Qatar Airways (Qatar) Qatari\n'], ['TVS', '  Travel Service/Smart Wings (Czech Rep.) Skytravel\n'], ['TPA', '  TAMPA Transportes Aereos Mercantiles Panamericanos (Colombia) Tampa\n'], ['UGX', '  East African Airlines (Uganda) Crane\n'], ['UTN', '  UTair-Ukraine (Ukraine) UT Ukraine\n'], ['LAO', '  Lao Airlines (Laos) Lao\n'], ['TCI', '  Turks Air Cargo (Turks and Caicos Islands) Kerrmont\n'], ['QXE', '  Horizon Air (USA) Horizon Air\n'], ['BCS', '  European Air Transport (Belgium) Eurotrans\n'], ['AWQ', '  Indonesia AirAsia (Indonesia) Wagon Air\n'], ['RPK', '  Royal Airlines (Pakistan) Royal Pakistan\n'], ['ORB', '  Orenair/Orenburg Airlines (Russia) Orenburg\n'], ['SYL', '  Yakutia Airlines (Russia) Air Yakutia\n'], ['JAV', '  Jordan Aviation (Jordan) Jordan Aviation\n'], ['DNU', '  DOT LT/Danu Oro Transportas (Lithuania) Danu\n'], ['OCA', '  Aserca Airlines (Venezuela) Arosca\n'], ['CAM', '  Camai Air/Village Aviation (USA) Air Camai\n'], ['TSD', '  TAF Linhas Aereas (Brazil) Tafi\n'], ['RNA', '  Nepal Airlines (Nepal) Nepal\n'], ['SYR', '  Syrian Arab Airlines (Syrian Arab Rep.) Syrianair\n'], ['FLI', '  Atlantic Airways (Faroe Islands) Faroeline\n'], ['REA', '  Stobart Air (Ireland) Aer Arann\n'], ['FWL', '  Florida West International Airways (USA) Flo West\n'], ['RPH', '  RPX Airlines/Republic Express Airlines (Indonesia) Public Express\n'], ['RJA', '  Royal Jordanian (Jordan) Jordanian\n'], ['RCT', '  R Airlines (Thailand) Green Sky\n'], ['RIO', '  Rio Linhas Aereas (Brazil) Rio Linhas\n'], ['RKT', '  Rayani Air (Malaysia) Blue Green\n'], ['ROT', '  Tarom Romanian Air Transport (Romania) Tarom\n'], ['CHQ', '  Chautauqua Airlines (USA) Chautauqua\n'], ['KMF', '  Kam Air (Afghanistan) Kamgar\n'], ['RFR', '  Royal Air Force (United Kingdom) Rafair (+ various others)\n'], ['ORF', '  Oman Royal Flight (Oman) Oman\n'], ['SKV', '  Sky Regional Airlines/Air Canada Express (Canada) Maple\n'], ['ABW', '  AirBridge Cargo Airlines (Russia) Airbridge Cargo\n'], ['CPN', '  Caspian Airlines Service Company (Iran) Caspian\n'], ['ROU', '  Air Canada Rouge (Canada) Rouge\n'], ['RPA', '  Republic Airlines (USA) Brickyard\n'], ['LRS', '  SANSA Servicios Aereos Nacionales SA (Costa Rica)\n'], ['BBR', '  Santa Barbara Airlines (Venezuela) Santa Barbara\n'], ['RZO', '  Sata International (Portugal) Air Azores\n'], ['TCF', '  Shuttle America (USA) Mercury\n'], ['SRR', '  Star Air (Denmark) White Star\n'], ['SBI', '  S7 Airlines/Siberia Airlines (Russia) Siberian Airlines\n'], ['SWW', '  Shovkoviy Shlyah Airlines (Ukraine) Way Aero\n'], ['IKM', '  Starbow Airlines (Ghana) Easy Shuttle\n'], ['SAA', '  South African Airways (South Africa) Springbok\n'], ['ACI', '  Aircalin/Air Caledonie International (New Caledonia) Aircalin\n'], ['CDG', '  Shandong Airlines (China) Shandong\n'], ['SUD', '  Sudan Airways (Sudan) Sudanair\n'], ['XLF', '  XL Airways France (France) Starway\n'], ['DTH', '  Tassili Airlines (Algeria) Tassili Air\n'], ['SEJ', '  SpiceJet (India) SpiceJet\n'], ['AWS', '  Arab Wings (Jordan) Arab Wings\n'], ['BCI', '  Blue Islands (United Kingdom) Blue Island\n'], ['SPA', '  Sierra Pacific Airlines (USA) Sierra Pacific\n'], ['CGL', '  Seagle Air (Slovakia) Seagle\n'], ['SAS', '  SAS Scandinavian Airlines System (Denmark/Norway/Sweden) Scandinavian\n'], ['TLM', '  Thai Lion Air (Thailand) Mentari\n'], ['MNP', '  Spirit of Manila Airlines (Philippines) Manila Sky\n'], ['BEL', '  Brussels Airlines (Belgium) Bee Line\n'], ['HKA', '  Superior Aviation (USA) Spend Air\n'], ['SLC', '  SALSA d\xe2\x80\x99Haiti (Haiti) Salsa\n'], ['SAT', '  SATA Air Acores (Portugal) Sata\n'], ['SIA', '  Singapore Airlines (Singapore) Singapore\n'], ['SQC', '  Singapore Airlines Cargo (Singapore) Singcargo\n'], ['CRL', '  Corsairfly (France) Corsair\n'], ['GMI', '  Germania (Germany) Germania\n'], ['AFL', '  Aeroflot Russian Airlines (Russia) Aeroflot\n'], ['SVA', '  Saudi Arabian Airlines (Saudi Arabia) Saudia\n'], ['NMB', '  Air Namibia (Namibia) Namibia\n'], ['SCX', '  Sun Country Airlines (USA) Sun Country\n'], ['TPU', '  Taca Peru (Peru) Trans Peru\n'], ['TMA', '  Trans Mediterranean Airways (Lebanon) Tango Lima\n'], ['EZE', '  Eastern Airways (United Kingdom) East Flight\n'], ['TIB', '  TRIP Linhas Aereas (Brazil) Trip\n'], ['TUA', '  Turkmenistan Airlines (Turkmenistan) Turkmenistan\n'], ['TVR', '  Tavrey Airlines/Tavria Aviakompania (Ukraine) Travey\n'], ['TJT', '  Twin Jet (France) Twinjet\n'], ['TAI', '  Taca International Airlines (El Salvador) Taca\n'], ['JAF', '  Jetairfly (Belgium) Beauty\n'], ['ATC', '  Air Tanzania (Tanzania) Tanzania\n'], ['LUR', '  Atlantis European Airways (Armenia)\n'], ['SCW', '  Malmo Aviation (Sweden) Scanwing\n'], ['THA', '  Thai Airways International (Thailand) Thai\n'], ['TSE', '  Transmile Air Services (Malaysia) Transmile\n'], ['TOL', '  TolAir Services (Puerto Rico) Tol Air\n'], ['AJA', '  AnadoluJet (Turkey) Anadolujet\n'], ['THY', '  Turkish Airlines (Turkey) Turk Air\n'], ['ANO', '  Airnorth Regional (Australia) Top End\n'], ['LAM', '  LAM (Mozambique) Mozambique\n'], ['THT', '  Air Tahiti Nui (French Polynesia) Tahiti Lines\n'], ['TVF', '  Transavia France (France) France Soleil\n'], ['TAP', '  TAP Portugal (Portugal) Air Portugal\n'], ['TDM', '  Tandem Aereo (Moldova) Tandem\n'], ['TGW', '  Tiger Airways (Singapore) Go Cat\n'], ['TSC', '  Air Transat (Canada) Air Transat\n'], ['TGW', '  Tiger Airways Australia (Australia) Go Cat\n'], ['TAR', '  Tunisair (Tunisia) Tunair\n'], ['TBA', '  Tibet Airlines (China) Tibet\n'], ['FWI', '  Air Caraibes (Guadeloupe/Martinique) French West\n'], ['TPC', '  Air Caledonie (New Caledonia) Air Cal\n'], ['SCO', '  Scoot (Singapore) Scooter\n'], ['TWG', '  Air-taxi europe (Germany) Twin-Goose\n'], ['EZY', '  easyJet (United Kingdom) Easy\n'], ['AIA', '  Avies (Estonia) Avies\n'], ['SVR', '  Ural Airlines (Russia) Sverdlovsk Air\n'], ['UAL', '  United Airlines (USA) United\n'], ['UBA', '  Myanma Airways (Myanmar) Unionair\n'], ['LCO', '  LAN Cargo (Chile) Lan Cargo\n'], ['HER', '  Hex\xe2\x80\x99Air (France) Hex Airline\n'], ['NAS', '  Nasair (Eritrea) Nasairways\n'], ['UKM', '  UM Air/Ukrainian Mediterranean Airlines (Ukraine) Ukraine Mediterrannee\n'], ['SEN', '  Sevenair (Tunisia) Sevenair\n'], ['GMT', '  Magnicharters (Mexico) Grupo Monterrey\n'], ['LMU', '  AlMasria Universal Airlines (Egypt) Almasria\n'], ['ALK', '  SriLankan Airlines (Sri Lanka) Sri Lankan\n'], ['TSO', '  Transaero Airlines (Russia) Trans Soviet\n'], ['HKE', '  Hong Kong Express (Hong Kong) Hongkong Shuttle\n'], ['BHS', '  Bahamasair (Bahamas) Bahamas\n'], ['KMV', '  UTair Express (Russia) Kominter\n'], ['AWE', '  US Airways (USA) Cactus\n'], ['JIA', '  PSA Airlines (USA) Blue Streak\n'], ['PDT', '  Piedmont Airlines (USA) Piedmont\n'], ['UTA', '  UTair Aviation (Russia) Utair\n'], ['REU', '  Air Austral (Reunion Island) Reunion\n'], ['UTP', '  Uni-Top Airlines (China) Uni-Top\n'], ['AEA', '  Air Europa (Spain) Europa\n'], ['BRQ', '  Buraq Air Transport (Libya) Buraq Air\n'], ['VCV', '  Conviasa (Venezuela) Conviasa\n'], ['RBY', '  Vision Airlines (USA) Ruby\n'], ['KRP', '  Carpatair (Romania) Carpatair\n'], ['VEC', '  Vensecar Internacional (Venezuela) Vensecar\n'], ['VOG', '  Voyager Airlines (Bangladesh) Voyager Air\n'], ['VOE', '  Volotea (Spain) Volotea\n'], ['TPS', '  TAPSA Transportes Aereos Petroleros SA (Argentina) Tapsa\n'], ['VAS', '  ATRAN Aviatrans Cargo Airlines (Russia) Atran\n'], ['VAU', '  Virgin Australia International Airlines (Australia) Vee Oz\n'], ['VIV', '  Viva Aerobus (Mexico) Aeroenlaces\n'], ['VAL', '  Voyageur Airways (Canada) Voyageur\n'], ['KPA', '  Henan Airlines (China) Kun Peng\n'], ['VJC', '  VietJet Air (Vietnam) Vietjetair\n'], ['VLM', '  VLM (Belgium) Rubens\n'], ['ALV', '  Aeropostal Alas de Venezuela (Venezuela) Alven\n'], ['VDA', '  Volga-Dnepr Airlines (Russia) Volda Dnepr\n'], ['VES', '  Vieques Air Link (Puerto Rico) Vieques\n'], ['VIM', '  Air VIA Bulgarian Airways (Bulgaria) Via Airways\n'], ['HVN', '  Vietnam Airlines (Vietnam) Vietnam Airlines\n'], ['TYR', '  Tyrolean Airways/Austrian Arrows (Austria) Tyrolean\n'], ['TCV', '  TACV Cabo Verde Airlines (Cape Verde) Cabo Verde\n'], ['VIR', '  Virgin Atlantic Airways (United Kingdom) Virgin\n'], ['VTA', '  Air Tahiti (French Polynesia) Air Tahiti\n'], ['TAO', '  Transportes Aeromar (Mexico) Trans Aeromar\n'], ['VRD', '  Virgin America (USA) Redwood\n'], ['VLG', '  Vueling Airlines (Spain) Vueling\n'], ['WDL', '  WDL Aviation (Germany) WDL\n'], ['ARA', '  Arik Air (Nigeria) Arik Air\n'], ['DNU', '  Danu Oro Transportas (Lithuania) Danu\n'], ['SWT', '  Swiftair (Spain) Swift\n'], ['BES', '  Aero Services Executive (France) Bird Express\n'], ['IRM', '  Mahan Air (Iran) Mahan Air\n'], ['WZZ', '  Wizz Air (Hungary) Wizz Air\n'], ['CJT', '  CargoJet Airways (Canada) Cargojet\n'], ['JAB', '  Air Bagan (Myanmar) Air Bagan\n'], ['KLC', '  KLM Cityhopper (Netherlands) City\n'], ['RWD', '  Rwandair Express (Rwanda) Rwandair\n'], ['ISV', '  Islena Airlines (Honduras)\n'], ['CWC', '  Centurion Air Cargo (USA) Challenge Cargo\n'], ['WIF', '  Wideroe Flyveselskap (Norway) Wideroe\n'], ['SWG', '  Sunwing Airlines (Canada) Sunwing\n'], ['TDX', '  TradeWinds Airlines (USA) Tradewinds Express\n'], ['LAL', '  Air Labrador (Canada) Lab Air\n'], ['EDW', '  Edelweiss Air (Switzerland) Edelweiss\n'], ['WIA', '  Winair/Windward Islands Airways (Sint Maarten) Windward\n'], ['SWA', '  Southwest Airlines (USA) Southwest\n'], ['MKU', '  Island Air (USA) Moku\n'], ['WEN', '  WestJet Encore (Canada) Encore\n'], ['WJA', '  WestJet (Canada) Westjet\n'], ['WSG', '  Wasaya Airways (Canada) Wasaya\n'], ['WOW', '  WOW air (Iceland) Wow Air\n'], ['BCY', '  CityJet (Ireland) City Ireland\n'], ['OMA', '  Oman Air (Oman) Oman Air\n'], ['MDJ', '  Jetran Air (Romania) Jetran Air\n'], ['VAZ', '  Red Wings Airlines (Russia) Remont Air\n'], ['TUI', '  TUIfly (Germany) TUI Jet\n'], ['OTJ', '  Fly Romania (Romania) Fly Romania\n'], ['DAP', '  Aerovias DAP (Chile) Dap\n'], ['KHO', '  Khors Aircompany (Ukraine) Aircompany Khors\n'], ['XAA', '  ARINC/Aeronautical Radio Inc. (USA)\n'], ['IAT', '  IATA/International Air Transport Association (Canada)\n'], ['KDC', '  KD Air (Canada) Kay Dee\n'], ['VLK', '  Vladivostok Air (Russia) Vladair\n'], ['KHH', '  Alexandria Airlines (Egypt)\n'], ['XXH', '  Special Ground Handling Service (USA)\n'], ['XXI', '  AEROTEL/Aeronautical Telecommunications (Jamaica)\n'], ['TAX', '  Thai AirAsia X (Thailand) Express Wing\n'], ['CCM', '  Air Corsica/Compagnie Corse Mediterranee (France) Corsica\n'], ['LNE', '  LAN Ecuador (Ecuador) Lan Ecuador\n'], ['JLJ', '  J-Air (Japan) J-Air\n'], ['JTE', '  JetEx/Australian Air Express (Australia) JetEx\n'], ['XAR', '  Xpress Air (Indonesia) Travel Express\n'], ['SXS', '  SunExpress (Turkey) Sun Express\n'], ['OZW', '  SkyWest Airlines (Australia) Ozwest\n'], ['SIT', '  SITA (Belgium)\n'], ['INX', '  Indonesia AirAsia X (Indonesia) IndonesianRedcap\n'], ['AXK', '  African Express Airways (Kenya) Express Jet\n'], ['KNE', '  Nas Air/Al-Khayala Airline (Saudi Arabia) Nas Express\n'], ['EXY', '  South African Express Airways (South Africa) Expresswayx\n'], ['VOI', '  Volaris (Mexico) Volaris\n'], ['AWA', '  Asia Wings (Kazakhstan) Asia Wings\n'], ['GMR', '  Golden Myanmar Airlines (Myanmar) Golden Myanmar\n'], ['TYA', '  Taimyr Air Company (Russia) Taimyr\n'], ['YZR', '  Yangtze River Express Airlines (China) Yangtze River\n'], ['IRK', '  Kish Air (Iran) Kishair\n'], ['LLM', '  Yamal Airlines (Russia) Yamal\n'], ['CFC', '  Canadian Armed Forces (Canada) Canforce\n'], ['OTL', '  South Airlines (Ukraine) Southline\n'], ['RSI', '  Air Sunshine (USA) Air Sunshine\n'], ['NTN', '  National Airways (South Africa) Natchair\n'], ['BSA', '  Air Bissau International (Guinea-Bissau) Bissau International\n'], ['ULG', '  U Airlines (Thailand)\n'], ['MGX', '  Montenegro Airlines (Montenegro) Montair\n'], ['CRQ', '  Air Creebec (Canada) Cree\n'], ['MCM', '  Heli Air Monaco (Monaco) Heli Air\n'], ['POT', '  Polet Cargo Airlines (Russia) Polet\n'], ['EGJ', '  Scenic Airlines (USA) Scenic\n'], ['MMZ', '  euroAtlantic airways (Portugal) Euroatlantic\n'], ['ASH', '  Mesa Airlines (USA) Air Shuttle\n'], ['ANE', '  Air Nostrum (Spain) Nostrum Air\n'], ['EZD', '  AirAsia Zest (Philippines) Zest Airways\n'], ['SMJ', '  AV Cargo (Zimbabwe)\n'], ['UDN', '  Dnieproavia (Ukraine) Dniepro\n'], ['AZN', '  Linea Aerea Amaszonas (Bolivia) Amaszonas\n'], ['MTZ', '  Mali Airways (Mali) Mali Airways\n'], ['DCP', '  Delta Connection Kenya (Kenya) Nilecat\n'], ['SWM', '  Sky Wings Asia Airlines (Cambodia) Sky Wings\n'], ['MON', '  Monarch Airlines (United Kingdom) Monarch\n'], ['FDN', '  Dolphin Air (United Arab Emirates) Flying Dolphin\n'], ['AZE', '  Arcus-Air Logistics (Germany) Arcus Air\n'], ['ESR', '  Eastar Jet (Korea \xe2\x80\x93 Rep. of) Eastar\n'], ['CSZ', '  Shenzhen Airlines (China) Shenzhen Air\n'], ['AAF', '  Aigle Azur (France) Aigle Azur\n'], ['ARC', '  Air Routing International (USA)\n'], ['GLA', '  Great Lakes Aviation (USA) Lakes Air\n'], ['RXA', '  Regional Express (Australia) Rex\n'], ['CNB', '  CityLine Hungary (Hungary) Cityhun\n'], ['NAY', '  NAYSA Navegacion y Servicios Aereos Canarios (Spain) Naysa\n'], ['AZQ', '  Silk Way Airlines (Azerbaijan) Silk Line\n'], ['LOC', '  Locair (USA) Locair\n'], ['AZS', '  Aviacon Zitotrans (Russia) Zitotrans\n'], ['PUN', '  Punto Azul (Equatorial Guinea) Punto Azul\n'], ['AWC', '  Titan Airways (United Kingdom) Zap\n'], ['AWI', '  Air Wisconsin (USA) Air Wisconsin\n'], ['GGN', '  Air Georgian/Air Alliance (Canada) Georgian']]

def readbyte():
	global index
	one_byte = f.read(1)
	if (one_byte == ""):
		print("\n\n")
		print(" .----------------.  .-----------------. .----------------. ")
		print("| .--------------. || .--------------. || .--------------. |")
		print("| |  _________   | || | ____  _____  | || |  ________    | |")
		print("| | |_   ___  |  | || ||_   \|_   _| | || | |_   ___ `.  | |")
		print("| |   | |_  \_|  | || |  |   \ | |   | || |   | |   `. \ | |")
		print("| |   |  _|  _   | || |  | |\ \| |   | || |   | |    | | | |")
		print("| |  _| |___/ |  | || | _| |_\   |_  | || |  _| |___.' / | |")
		print("| | |_________|  | || ||_____|\____| | || | |________.'  | |")
		print("| |              | || |              | || |              | |")
		print("------------------------------------------------------------")
		print("I am Reading Nothing ,So : It is The End of File Or A big Problem.")
		print("We Will implement a feature in future to inspect the End of The File")	
		print("Thanks For Using Our App")
		sys.exit()
	
	number = ord(one_byte)
	index = index + 1
	return number

def SIX_BITS_CHAR(code):
	ind        = (code & 0x30) >> 4
	letter_num = (code & 0xF)

	if(letter_num == 0):
		if(ind == 0):
			return " "
		elif(ind == 1):
			return 'P'
		elif(ind == 2):
			return " "
		elif(ind == 3):
			return '0'		
	elif(letter_num	== 1):
		if(ind == 0):
			return 'A'
		elif(ind == 1):
			return	'Q'
		elif(ind == 2):
			return " "
		elif(ind == 3):
			return '1'
	elif(letter_num	== 2):
		if(ind == 0):
			return 'B'
		elif(ind == 1):
			return 'R'	
		elif(ind == 2):
			return " "
		elif(ind == 3):
			return '2'
	elif(letter_num	== 3):
		if(ind == 0):
			return 'C'
		elif(ind == 1):
			return	'S'
		elif(ind == 2):
			return " "
		elif(ind == 3):
			return '3'
	elif(letter_num	== 4):
		if(ind == 0):
			return 'D'
		elif(ind == 1):
			return	'T'
		elif(ind == 2):
			return " "
		elif(ind == 3):
			return '4'
	elif(letter_num	== 5):
		if(ind == 0):
			return 'E'
		elif(ind == 1):
			return	'U'
		elif(ind == 2):
			return " "
		elif(ind == 3):
			return '5'
	elif(letter_num	== 6):
		if(ind == 0):
			return 'F'
		elif(ind == 1):
			return 'V'	
		elif(ind == 2):
			return " "
		elif(ind == 3):
			return '6'
	elif(letter_num	== 7):
		if(ind == 0):
			return 'G'
		elif(ind == 1):
			return	'W'
		elif(ind == 2):
			return " "
		elif(ind == 3):
			return '7'
	elif(letter_num	== 8):
		if(ind == 0):
			return 'H'
		elif(ind == 1):
			return	'X'
		elif(ind == 2):
			return " "
		elif(ind == 3):
			return '8'
	elif(letter_num	== 9):
		if(ind == 0):
			return 'I'
		elif(ind == 1):
			return	'Y'
		elif(ind == 2):
			return " "
		elif(ind == 3):
			return '9'
	elif(letter_num	== 10):
		if(ind == 0):
			return 'J'
		elif(ind == 1):
			return	'Z'
		elif(ind == 2):
			return " "
		elif(ind == 3):
			return '10'
	elif(letter_num	== 11):
		if(ind == 0):
			return 'K'
		elif(ind == 1):
			return	" "
		elif(ind == 2):
			return " "
		elif(ind == 3):
			return " "
	elif(letter_num	== 12):
		if(ind == 0):
			return 'L'
		elif(ind == 1):
			return	" "
		elif(ind == 2):
			return " "
		elif(ind == 3):
			return " "
	elif(letter_num	== 13):
		if(ind == 0):
			return 'M'
		elif(ind == 1):
			return " "
		elif(ind == 2):
			return " "
		elif(ind == 3):
			return " "
	elif(letter_num	== 14):
		if(ind == 0):
			return 'N'
		elif(ind == 1):
			return " "	 
		elif(ind == 2):
			return " "
		elif(ind == 3):
			return " "
	elif(letter_num	== 15):
		if(ind == 0):
			return 'O'
		elif(ind == 1):
			return " "
		elif(ind == 2):
			return " "
		elif(ind == 3):
			return " "


def MODE3_A_REPLAY_OCTAL(cat):
	MODE3_A1 = readbyte()
	MODE3_A2 = readbyte()
	MODE3_A_REPLAY = ((MODE3_A1 << 8) | MODE3_A2) & 4095  # 4095 = 0b0000 1111 1111 1111

	MODE3_A_V = (MODE3_A1 & 128)
	MODE3_A_G = (MODE3_A1 & 64)
	MODE3_A_L = (MODE3_A1 & 32)

	if(cat == 1):
		print("+---I001/070 [Mode-3A Code in Octal Representation]")
	elif(cat == 48):
		print("+---I048/070 [Mode-3A Code in Octal Representation]")

	if(MODE3_A_V):
		print(" |____V : 1 :Code Not Validate")
	else:
		print(" |____V : 0 :Code Validate")
	if(MODE3_A_G):
		print(" |____G : 1 :Code Garbled")
	else:
		print(" |____G : 0 :Code Not Garbled")
	if(MODE3_A_L):
		if (cat == 1):
			print(" |____L : 1 :Smoothed Mode3_A Code Provided By Local Tracker")
		elif(cat == 48):
			print(" |____L : 1 :Mode3_A Code Not Extracted during the last scan")
	else:
		print(" |____L : 0 :Mode3_A Code As Derived From the Reply Of Transponder")

	print(" |____bit13: 0 : [Spare Bit Always Set to 0]")
		
	print(" |____Mode3_A reply In Octal : %o" % MODE3_A_REPLAY)
	print("		|____ Decimal : %d" % MODE3_A_REPLAY)

def MODE_C_BINARY():
	MOD_C_CODE1 = readbyte()
	MOD_C_CODE2 = readbyte()
	MOD_C_CODE  = ( MOD_C_CODE1 << 8) | MOD_C_CODE2
	MOD_C_CODE_HEIGHT = (MOD_C_CODE & 16383)
	MOD_C_CODE_V = (MOD_C_CODE1 & 128)
	MOD_C_CODE_G = (MOD_C_CODE1 & 64)
	print("+---I001/090 : [Mode C Code In Binary Representation]")
	if (MOD_C_CODE_V):
 		print(" |____MODE_C_CODE_V : 1 : [Code Not Validated]")
 	else:
 		print(" |____MODE_C_CODE_V : 0 : [Code Validated]")
 	if (MOD_C_CODE_G):
 		print(" |____MODE_C_CODE_G : 1 : [Garbled Code]")
 	else:
 		print(" |____MODE_C_CODE_G : 0 : [Default (No Garbled)]")

 	if (MOD_C_CODE_HEIGHT):
 		print(" |____MODE_C_CODE_HEIGHT 	: %.2f FL: [Mode-C Height]" % (MOD_C_CODE_HEIGHT * 1/4))
 			# bit-1 (LSB) = 1/4 FL = 25 feet. (Radar Data Exchange Part-2a Document)

def TRUNCATED_TIME():
	TRUNCATED_TIME1 = readbyte()
	TRUNCATED_TIME2 = readbyte()
	TRUNCATED_TIME  = (TRUNCATED_TIME1 << 8) | TRUNCATED_TIME2	
 	print("+---I001/141 [Truncated Time Of Day]: %.2f sec" % (TRUNCATED_TIME * 1/128))

def RADAR_PLOT_CHARAC(cat):
	if (cat == 1):

		RADAR_PLOT_CARAC = readbyte()
		DATA = RADAR_PLOT_CARAC >> 1
		print("+---I001/130 : [Radar Plot Charac] : %d" % DATA)
		if(RADAR_PLOT_CARAC & 1):
			RADAR_PLOT_CARAC_EXT = readbyte()
			print(" |____Extension Byte %d ]" % RADAR_PLOT_CARAC_EXT)
		else:
			print(" |____No Extension Byte")	
	elif(cat == 48):
		RADAR_PLOT_CARAC = readbyte()
		print("+---I048/130 : [Radar Plot Charac] : %d" % RADAR_PLOT_CARAC)	
		SRL = (RADAR_PLOT_CARAC & 128)
		SRR = (RADAR_PLOT_CARAC & 64)
		SAM = (RADAR_PLOT_CARAC & 32)
		PRL = (RADAR_PLOT_CARAC & 16)
		PAM = (RADAR_PLOT_CARAC & 8)
		RPD = (RADAR_PLOT_CARAC & 4)
		APD = (RADAR_PLOT_CARAC & 2)
		FX  = (RADAR_PLOT_CARAC & 1)

		if(SRL):
			Subfield_1 = readbyte()
			print(" |____SSR Plot Runlength : %.2f deg" % (Subfield_1 * 0.044))
		if(SRR):
			Subfield_2 = readbyte()
			print(" |____Number Of Recieved Replies for M(SSR): %d " % Subfield_2)
		if(SAM):
			Subfield_3 = readbyte()
			print(" |____Amplitude of M(SSR): %d dBm" % Subfield_3)
		if(PRL):
			Subfield_4 = readbyte()
			print(" |____Primary Plot Runlength: %.2f deg" % (Subfield_4 * 0.044))
		if(PAM):
			Subfield_5 = readbyte()
			print(" |____Amplitude of Primary Plot: %d dBm" % Subfield_5)
		if(RPD):
			Subfield_6 = readbyte()
			if(Subfield_6 & 128):
				print(" |____Diffrence in Range between PSR & SSR plot: -%d" % (Subfield_6 & 0x7F))							
			else:
				print(" |____Diffrence in Range between PSR & SSR plot: %d" % Subfield_6)							
		if(APD):
			Subfield_7 = readbyte()
			print(" |____Diffrence in Azimuth between PSR & SSR plot: %.2f deg" % (Subfield_7 * 0.044))
		if(FX):
			print(" |____ Extension Exists")
			Radar_Ext = readbyte()
			print(" 	|____ %s" % bin(Radar_Ext))

			

def POLAR_CORD(cat):
	MSPOLAR_CORD1 = readbyte()
	MSPOLAR_CORD2 = readbyte()
	MSPOLAR_CORD3 = readbyte()
	MSPOLAR_CORD4 = readbyte()

	
	RHO_MSPOLAR_CORD  = (MSPOLAR_CORD1 << 8) | MSPOLAR_CORD2
	THETA_MSPOLAR_CORD  = (MSPOLAR_CORD3 << 8) | MSPOLAR_CORD4
	
	if(cat == 1):
		print("+---I001/040 [POSITION IN POLAR CORDINATES]:")
	elif(cat == 48):
		print("+---I048/040 [POSITION IN POLAR CORDINATES]:")

	print(" |____ RHO_MSPOLAR_CORD  : %d " % (RHO_MSPOLAR_CORD ))
	if(cat == 1):
		print(" |  		|____%.4f NM" % (RHO_MSPOLAR_CORD * 1/128))
	elif(cat == 48):
		print(" |  		|____%.4f NM" % (RHO_MSPOLAR_CORD * 1/256))
	print(" |____ THETA_MSPOLAR_CORD: %d " % (THETA_MSPOLAR_CORD))
	print("   		|____%.4f deg" % (THETA_MSPOLAR_CORD * 0.0055))


def CARTESIAN_CORD(cat):

	CARTESIAN_CORD1 = readbyte()
	CARTESIAN_CORD2 = readbyte()
	CARTESIAN_CORD3 = readbyte()
	CARTESIAN_CORD4 = readbyte()

	X_CORD  = (CARTESIAN_CORD1 << 8) | CARTESIAN_CORD2
	Y_CORD  = (CARTESIAN_CORD3 << 8) | CARTESIAN_CORD4
	
	if(cat == 1):
		print("+---I001/042: [CARTESIAN CORD]")
	elif(cat == 48):
		print("+---I048/042: [CARTESIAN CORD]")
	print("X_CORD %s :" % bin(X_CORD))
	print("Y_CORD %s :" % bin(Y_CORD))
	
	if(CARTESIAN_CORD1 & 128):
		if(cat == 1):
			print(" |____ CARTESIAN_X_CORD : -%.2f NM" % ((X_CORD & 32767)) * 1/64)
			#just do not take the last bit in considiration bcz it is a Sign bit not included in the number.
		elif(cat == 48):
			print(" |____ CARTESIAN_X_CORD : -%.2f NM" % ((X_CORD & 32767)) * 1/128)

	else:
		if(cat == 1):
			print(" |____ CARTESIAN_X_CORD : -%.2f NM" % (X_CORD  * 1/64))
			#just do not take the last bit in considiration bcz it is a Sign bit not included in the number.
		elif(cat == 48):
			print(" |____ CARTESIAN_X_CORD : -%.2f NM" % (X_CORD  * 1/128))

	if(CARTESIAN_CORD3 & 128):
		if(cat == 1):
			print(" |____ CARTESIAN_Y_CORD : -%.2f NM" % ((Y_CORD & 32767)) * 1/64)
			#just do not take the last bit in considiration bcz it is a Sign bit not included in the number.
		elif(cat == 48):
			print(" |____ CARTESIAN_Y_CORD : -%.2f NM" % ((Y_CORD & 32767)) * 1/128)

	else:
		if(cat == 1):
			print(" |____ CARTESIAN_Y_CORD : -%.2f NM" % (Y_CORD  * 1/64))
			#just do not take the last bit in considiration bcz it is a Sign bit not included in the number.
		elif(cat == 48):
			print(" |____ CARTESIAN_Y_CORD : -%.2f NM" % (Y_CORD  * 1/128))




def TRACK_VELOCITY(cat):
	TRACK_VELOCITY1 = readbyte()
	TRACK_VELOCITY2 = readbyte()
	TRACK_VELOCITY3 = readbyte()
	TRACK_VELOCITY4 = readbyte()

	GROUND_SPEED  		= (TRACK_VELOCITY1 << 8) | TRACK_VELOCITY2
	CALCULATED_HEADING 	= (TRACK_VELOCITY3 << 8) | TRACK_VELOCITY4

	if(cat == 1):
		print("+---I001/200 : [TRACK VELOCITY IN POLAR CORD]:")
	elif(cat == 48):
		print("+---I048/200 : [TRACK VELOCITY IN POLAR CORD]:")

	print(" |____ GROUND_SPEED : %d : [Ground Speed]" % (GROUND_SPEED ))
	print(" |		|____%.2f kt" % (GROUND_SPEED * 0.22 ))
	print(" |____ HEADING      : %d : [Heading]" % (CALCULATED_HEADING ))
	print(" 		|____%.2f deg" % (CALCULATED_HEADING * 0.005 ))

def RECEIVED_POWER():
	RECEIVED_POWER = readbyte()
	print("+---I001/131 [RECIEVED_POWER]: %d dBm" % RECIEVED_POWER)

def RADIAL_DOPPLER_SPEED(cat):
	if(cat == 1):
		RADIAL_DOPPLER_SPEED = readbyte()
		print("+---I001/120 [RADIAL DOPPLER SPEED]: %d " % RADIAL_DOPPLER_SPEED)		
	elif(cat == 48):
		print("+---I048/120 [RADIAL DOPPLER SPEED]")
		PRIMARY = readbyte()
		if(PRIMARY & 128):
			print(" |____ CAL: 1 : Calculated Doppler Speed Exists")
			CAL1 = readbyte()
			CAL2 = readbyte()

			CAL  = (CAL1<<8) | CAL2
			if(CAL1 & 128):
				print(" | 	|____D:1:Doppler Speed Doubtful ")
			else:
				print(" | 	|____D:0:Doppler Speed Valid ")
			print(" | 	|____bits15-11: Spare bits set to 0 ")
				
			CAL_SPEED = (CAL & 0x1FF)
			if(CAL & 0x200):
				print(" | 	|____Doppler Speed : -%d m/sec" % CAL_SPEED)
			else:
				print(" | 	|____Doppler Speed :  %d m/sec" % CAL_SPEED)



		if(PRIMARY & 64):
			print(" |____ RDS: 1 : Raw Doppler Speed Exists")
			REP = readbyte()
			while(REP):
				print(" | 	|	(Data%d)" % REP)
				DOP1=readbyte()
				DOP2=readbyte()
				DOP = (DOP1<<8) | DOP2
				print(" | 	|____Doppler Speed: %d m/sec" % DOP)
				AMB1=readbyte()
				AMB2=readbyte()
				AMB = (AMB1<<8) | AMB2
				print(" | 	|____Ambiguity Range: %d m/sec" % AMB)
				FRQ1= readbyte()
				FRQ2= readbyte()
				FRQ = (FRQ1<<8) | FRQ2
				print(" | 	|____Transmitter Frequency: %d Mhz" % FRQ)

				REP = REP - 1
		print(" |____ 1-6bits: 0 : Spare bits")
		






def TRACK_STATUS(cat):
	TRACK_STATUS = 	readbyte()
	if(cat == 1):
		print("+---I001/170 [TRACK STATUS] :")

		if(TRACK_STATUS & 128):
			print(" |____ CON : 1 : Track in initialisation phase")
		else:	 	
			print(" |____ CON : 0 : Track Confirmed") 		
		if(TRACK_STATUS & 64):
			print(" |____ RAD : 1 : SSR Combined Track")
		else:
			print(" |____ RAD : 0 : Primary Track")
		if(TRACK_STATUS & 32):
			print(" |____ MAN : 1 : Aircraft Manoeuvring")
		else:
			print(" |____ MAN : 0 : Deafault")
		if(TRACK_STATUS & 16):
			print(" |____ DOU : 1 : Doubtful plot to Track Association")
		else:
			print(" |____ DOU : 0 : Default")
		if(TRACK_STATUS & 8):
			print(" |____ RDPC: 1 : RDP (Radar Data Processing) chain 2")
		else:
			print(" |____ RDPC: 0 : RDP (Radar Data Processing) chain 1")
		print(" |____ bit-3 : Spare bit set to 0")	
		if(TRACK_STATUS & 2):
			print(" |____ GHO: 1 : Ghost Track")
		else:
			print(" |____ GHO: 0 : Default")

		if(TRACK_STATUS & 1):
			print(" |____ Extension Data Found:")
			TRACK_STATUS2 = readbyte()
			if(TRACK_STATUS2 & 128):
				print("   |____ (Extension) TRE: 1 : Last Report for a Track")
			else:
				print("   |____ (Extension) TRE: 0 : Default")
			print("   |____ (Extension) bits 0-7 : Spare Bits set To 0")
			if(TRACK_STATUS2 & 1):
				TRACK_STATUS3 = readbyte()
				print("     |____ There a Second Extension: %d " % TRACK_STATUS3)
			else:
				print("     |____ Second Extension Does Not Exist")
		else:
			print(" |____ FX : 0 : Extension Not Exist")

	
	elif(cat == 48):
		print("+---I048/170 [TRACK STATUS] :")				
		if(TRACK_STATUS & 128):
			print(" |____ CNF : 1 : Tentative Track")
		else:	 	
			print(" |____ CNF : 0 : Confirmed Track")

		RAD = (TRACK_STATUS & 96) 	
		if(RAD == 96):
			print(" |____ RAD : 11 : Invalid Track")
		elif(RAD == 64):
			print(" |____ RAD : 10 : SSR/Mode S Track")
		elif(RAD == 32):
			print(" |____ RAD : 01 : PSR Track")	
		elif(RAD == 0):
			print(" |____ RAD : 00 : Combined Track")
				
		if(TRACK_STATUS & 16):
			print(" |____ DUO : 1 : Low Confidence in plot to track Confidence")
		else:
			print(" |____ DUO : 0 : Normal Confidence")

		if(TRACK_STATUS & 8):
			print(" |____ MAH : 1 : Horizontal Manoeuvre Sensed")
		else:
			print(" |____ MAH : 0 : No Horizontal Manoeuvre Sensed")


		CDM = (TRACK_STATUS & 6)	
		if(CDM == 0):
			print(" |____ CDM: 00 : Maintaining Mode")
		elif(CDM == 2):
			print(" |____ CDM: 01 : Climbing Mode")
		elif(CDM == 4):
			print(" |____ CDM: 10 : Descending Mode")	
		elif(CDM == 6):
			print(" |____ CDM: 11 : Invalid Mode")

		if(TRACK_STATUS & 1):
			print(" |____ Extension Data Found:")
			TRACK_STATUS2 = readbyte()
			if(TRACK_STATUS2 & 128):
				print("   |____ (Extension) TRE: 1 : End Of Track Lifetime")
			else:
				print("   |____ (Extension) TRE: 0 : Track Still Alive")

			if(TRACK_STATUS2 & 64):
				print("   |____ (Extension) GHO: 1 : Ghost Target Track")
			else:
				print("   |____ (Extension) GHO: 0 : True (Not Ghost) Target Track")

			if(TRACK_STATUS2 & 32):
				print("   |____ (Extension) SUP: 1 : Track Maintained With Track infos from Neighbouring Node B On The cluster")
			else:
				print("   |____ (Extension) SUP: 0 : No Infos Maintained With Track from Neighbouring Node B ")		

			if(TRACK_STATUS2 & 16):
				print("   |____ (Extension) TCC: 1 : Slant Range Correction + Suitable Projection Techniques Used To track in 2D")	
			else:
				print("   |____ (Extension) TCC: 0 : Tracking Performed in Radar Plane (No Slant Range Correction + No StereoGeographical Projection)")						
			
			print("   |____ (Extension) bits4,3,2 set to 0")

			if(TRACK_STATUS2 & 1):	
				TRACK_STATUS3 = readbyte()
				print("     |____ There a Second Extension: [%s] " % bin(TRACK_STATUS3))
			else:
				print(" |____ FX : 0 : Second Extension Not Exist")





def TRACK_QUALITY(cat):
	if (cat == 1):
		#global index
		TRACKQ     = readbyte()
		#print TRACK_QUALITY
		TRACK_QUALITY_IND = TRACKQ >> 1

		print("+---I001/210 [TRACK QUALITY INDICATOR] : %d" % TRACK_QUALITY_IND)
		if (TRACKQ & 1):
			TRACK_QUALITY_EXTENSION = readbyte()
			print(" |____ Extension Byte: %d" % TRACK_QUALITY_EXTENSION)
		else:
			print(" |____ FX : 0 : Extension Not Exist")	
		

		#print ("index is : %d" % index)
	elif(cat == 48):

		 SIGMA_X = readbyte()
		 SIGMA_Y = readbyte()
		 SIGMA_V = readbyte()
		 SIGMA_H = readbyte()
		 print("+---I048/210 [TRACK QUALITY]")
		 print(" |____ Sigma X (Standard Deviation On Horizontal axis): %.2f NM"  % (SIGMA_X * 1/128))	
		 print(" |____ Sigma Y (Standard Deviation On Vertical axis)  : %.2f NM"  % (SIGMA_Y * 1/128))
		 print(" |____ Sigma V (Standard Deviation On The GroundSpeed): %.2f kt"  % (SIGMA_V * 0.22))
		 print(" |____ Sigma X (Standard Deviation On Horizontal axis): %.2f deg" % (SIGMA_H * 0.08789))

def MODE_2_CODE(cat):
	MODE_2_CODE1 = readbyte()
	MODE_2_CODE2 = readbyte()
	MODE_2_CODE  = (MODE_2_CODE1 << 8) |  MODE_2_CODE2
	MODE_2_CODE_OCTAL  =  (MODE_2_CODE & 0xFFF) # 0xFFF = 4095

	if(cat == 1):

		print("+---I001/050 [MODE-2 CODE IN OCTAL]")
	elif(cat == 48):
		print("+---I048/050 [MODE-2 CODE IN OCTAL]")

	if(MODE_2_CODE1 & 128):
		print(" |____ V: 1 : Not Validated")
	else:
		print(" |____ V: 0 : Code Validated")

	if(MODE_2_CODE1 & 64):
		print(" |____ G: 1 : Garbled Code")
	else:
		print(" |____ G: 0 : Default")

	if(MODE_2_CODE1 & 32):
		print(" |____ L: 1 : Mode-2 Code Derived From the Reply Of The Transponder")

	print(" |____ Mode2_code : [%s]" % bin(MODE_2_CODE_OCTAL))	

def MODE_3_CONF(cat):
	MCODE_3_CONFIDENCE1 = readbyte()
	MCODE_3_CONFIDENCE2 = readbyte()

	MCODE_3_CONFIDENCE  = (MCODE_3_CONFIDENCE1 << 8) | MCODE_3_CONFIDENCE2
	MCODE_3_CONFIDENCE_IND = MCODE_3_CONFIDENCE >> 4

	if (cat == 1):
		print("+---I001/080 [MCODE_3A_CONFIDENCE] :")
	elif(cat == 48):
		print("+---I048/080 [MCODE_3A_CONFIDENCE] :")

	print(" |____ MCODE-3A CONFIDANCE INDICATOR : [%s]" % bin(MCODE_3_CONFIDENCE_IND))
	print(" |____ bits 13-16: Spare bits set to 0")

def MODE_C_CODE_CONF(cat):
	MODE_C_CODE_AND_CODE_CONF1 = readbyte()
	MODE_C_CODE_AND_CODE_CONF2 = readbyte()
	MODE_C_CODE_AND_CODE_CONF3 = readbyte()
	MODE_C_CODE_AND_CODE_CONF4 = readbyte()

	MODE_C_CODE_1_16  = (MODE_C_CODE_AND_CODE_CONF1 << 8) | MODE_C_CODE_AND_CODE_CONF2
	MODE_C_CODE_17_32 =	(MODE_C_CODE_AND_CODE_CONF3 << 8) | MODE_C_CODE_AND_CODE_CONF4

	MODE_C_GRAY 					=  MODE_C_CODE_17_32 >> 4
	MODE_C_CODE_QUALITY_PULSE 		=  MODE_C_CODE_1_16 >> 4

	MODE_C_V = (MODE_C_CODE_AND_CODE_CONF1 & 128)
	MODE_C_G = (MODE_C_CODE_AND_CODE_CONF1 & 64)

	if(cat == 1):
		print("+---I001/100 [MODE-C Code & Confidence Indicator]:")
	elif(cat == 48):
		print("+---I048/100 [MODE-C Code & Confidence Indicator]:")

	if(MODE_C_V):	
		print(" |____ V: 1 : Code Not Validated")
	else:
		print(" |____ V: 0 : Code Validated")
	if(MODE_C_G):
		print(" |____ G: 1 : Garbled Code")
	else:
		print(" |____ G: 0 : Default")

	print(" |____ Mode-C replay in Gray Notation" % MODE_C_GRAY)
	print(" |____ Quality Pulse :[%s]" % bin(MODE_C_CODE_QUALITY_PULSE))

def MODE_2_IND(cat):
	MODE_2_CONFIDENCE_IND1 = readbyte()
	MODE_2_CONFIDENCE_IND2 = readbyte()

	MODE_2_CONF = (MODE_2_CONFIDENCE_IND1 << 8) | MODE_2_CONFIDENCE_IND2
	MODE_2_CONF_QUALITY = MODE_2_CONF >> 4

	if(cat == 1):
		print("+---I001/060 [Mode-2 Code Confidence Indicator]")
	elif(cat == 48):
		print("+---I048/060 [Mode-2 Code Confidence Indicator]")

	print(" |____ Quality Pulse %s" % bin(MODE_2_CONF_QUALITY))
	print(" |____ bits 13-16: Spare bits set to 0")

def WARNING(cat):
	WARNING1 = readbyte()
	WAR = WARNING1 >> 1
	if(cat == 1):
		print("+---I001/030 [Warning Code]: [%s]" % bin(WAR))
	elif(cat == 48):
		print("+---I048/030 [Warning Code]: [%s]" % bin(WAR))

	print("\nN.B: See The Documentation To Know More About Warnings Bits\n")

	
	if(WARNING1 & 1):
		EXT = readbyte()
		print(" |____ WARNING EXTENSION BYTE: [%s]" % bin(EXT))


def X_PULSE():
	print("+---I001/150 [X-PULSE] Exists:")
	X_PULSE = readbyte()
	if(X_PULSE & 128):
		print(" |____ XA : 1 : X-Pulse Received in Mode-3A Reply")
	else:	
		print(" |____ XA : 0 : Default")
	print(" |____ bit-7 : Set to 0")	
	if(X_PULSE & 32):
		print(" |____ XC : 1 : X-Pulse Received in Mode-C Reply")	
	else:
		print(" |____ XC : 0 : Default")

	print(" |____ bits-5-4 : Set to 0")
	
	if(X_PULSE & 4):
		print(" |____ X2 : 1 : X-Pulse Received in Mode-2 Reply")
	else:	
		print(" |____ X2 : 0 : Default")

	print(" |____ bits2-1 : Set to 0")			
	
def READ_SIC_SAC(cat):
	if (cat == 1):
		print ("+---I001/010 [Data Source Identifier]")
	elif(cat == 48):
		print ("+---I048/010 [Data Source Identifier]")
	SAC = readbyte()
	print(" |____ SAC : %d" % SAC)
	SIC = readbyte()
	print(" |____ SIC : %d\n" % SIC)	

def READ_DESCRIPTOR(cat):
	global track
	global plot

	if(cat == 48):
		track = 0
		plot  = 0 

	DES1 = readbyte()
	if(cat == 1):
		print("+---I001/020 [Target Report Descriptor] %s: " % bin(DES1))
	elif(cat == 48):
		print("+---I048/020 [Target Report Descriptor] %s: " % bin(DES1))
	if (DES1 & 1):  # Test if the Extension bit is Set
		DES2 = readbyte()
		print("+---DES2 %s: 1 : [Target Report Descriptor]" % bin(DES2))
	
	'''
	Here we Get TYP bit
	'''
	if (cat == 48):
		TYP = DES1 >> 5
		if (TYP == 7):
			print(" |____ DES.TYP : 111 : ModeS Roll-Call+PSR")
		elif(TYP == 6):
			print(" |____ DES.TYP : 110 : ModeS All-Call+PSR")
		elif(TYP == 5):
			print(" |____ DES.TYP : 101 : Single ModeS Roll-Call")
		elif(TYP == 4):
			print(" |____ DES.TYP : 100 : Single ModeS All-Call")
		elif(TYP == 3):
			print(" |____ DES.TYP : 011 : SSR+ PSR Detection")
		elif(TYP == 2):
			print(" |____ DES.TYP : 010 : Single SSR detection")
		elif(TYP == 1):
			print(" |____ DES.TYP : 001 : Single PSR detection")
		elif(TYP == 0):
			print(" |____ DES.TYP : 000 : No detection")

											   

	elif(cat == 1):
			
		if (DES1 & 128):
			print(" |____ DES.TYP : 1 : There is Track information (Not Plot)")
			track = 1
			plot  = 0
		else:
			print(" |____DES.TYP : 0 :There is Plot information  (Not Track)")
			plot  = 1
			track = 0

	if (cat == 48):
		if(DES1 & 16):
			print(" |____ DES.SIM : 1 : Simulated Target Report ")
		else:
			print(" |____ DES.SIM : 0 : Actual Target Report ")
		
		if(DES1 & 8):
			print(" |____ DES.RDP : 1 : Report From RDP Chain 2 ")
		else:
			print(" |____ DES.RDP : 0 : Report From RDP Chain 1 ")
	
	elif (cat == 1):
		'''
		Here we Get SIM bit
		'''	
		if(DES1 & 64):
			if (track):	
				print(" |____ DES.SIM : 1 : Simulated Track \n")	
			if(plot):
				print(" |____ DES.SIM : 1 : Simulated Plot \n")

		else:		
			if (track):	
				print(" |____ DES.SIM : 0 : Actual Track ")	
			if(plot):
				print(" |____ DES.SIM : 0 : Actual Plot ")
	
		'''
		Here we Get SSR/PSR bits
		'''
		Test = (DES1 & 48) >> 4		
		
		if(Test == 3 ):
				print(" |____ DES.SSR/PSR : 11 : Primary + Secondary Detection ")
		
		if(Test == 2):
			
			print(" |____ DES.SSR/PSR : 10 : Secondary Detection ")		

		if(Test == 1):
			print(" |____ DES.SSR/PSR : 01 : Primary Detection ")

		if(Test == 0):

			print(" |____ DES.SSR/PSR : 00 : No Detection ")	

		'''
		Here we Get ANT bit
		'''	
		if(DES1 & 8):
			print(" |____ DES.ANT : 1 : Report from Antenna 2 ")
		else:
			print(" |____ DES.ANT : 0 : Report from Antenna 1 ")	

	if(DES1 & 4):
		print(" |____ DES.SPI : 1 : Special Position Identification ")
	else:
		print(" |____ DES.SPI : 0 : Default (No SPI) ")
	if(DES1 & 2):
		if (cat == 1):
			print(" |____ DES.RAB : 1 : Track/Plot from a Fixed Trasnponder ")
		elif(cat == 48):
			print(" |____ DES.RAB : 1 : Report from a Fixed Trasnponder (Field Monitor) ")
	
	else:
		if (cat == 1):
			print(" |____ DES.RAB : 0 : Default (Track/Plot Not From Fixed Transponder) ")
		elif(cat == 48):
			print(" |____ DES.RAB : 0 : Report from aircraft transponder")
	
	if(DES1 & 1):
		DES2 = readbyte()
		print(" |____ DES.FX : 1 : Extension %s exists" % bin(DES2))
	else:
		print(" |____ DES.FX : 0 : Extension Does not exist")		

	if(cat == 1):
		print("-----------------------------------------------------------------")		
		print("DES.TYP bit (Track/Plot) decides The Order of the Next Data Items")		
		print("-----------------------------------------------------------------")
	
def TRACK_NUMBER(cat):
	if(cat == 1):
		print ("Track :")
		TRACKN1 = readbyte()
		TRACKN2 = readbyte()
		TRACKN  = (TRACKN1 << 8) | TRACKN2
		print("+---I001/161 [TRACKN NUMBER]: %d " % TRACKN)
	elif(cat == 48):
		TRACKN1 = readbyte()
		TRACKN2 = readbyte()
		TRACKN  = (TRACKN1 << 8) | TRACKN2
		print("+---I048/161 [TRACKN NUMBER]: %d " % TRACKN)

def FLIGHT_LEVEL():
	FL1 = readbyte()
	FL2 = readbyte()
	FL   = (FL1 << 8) | (FL2)
	print("+---I048/090 [FLIGHT LEVEL IN BINARY REPRESENTATION]: %s" % bin(FL))

	FL_V = (FL1 & 128)
	FL_L = (FL1 & 64)

	if(FL_V):
		print(" |____ V: 1 : Code not Validated")
	else:
		print(" |____ V: 0 : Code Validated")

	if(FL_L):
		print(" |____ L: 1 : Code Garbled")
	else:
		print(" |____ L: 0 : Default (Code Not Garbled)")

	LEV = (FL & 0x3FFF)
	print(" |____ Flight Level : (%d) %.2f FL" % (LEV , (LEV * 1/4)))			   

def AIRCRAFT_ADD():
	air_craft = readbyte()

	add1      = readbyte()
	add2	  = readbyte()

	address = (add1 << 8) | add2	

	print("+---I048/220 [Aircraft Address]:")

	print(" |____Aircraft: 0x%x (%d)" % (air_craft, air_craft))
	print(" |____Address : 0x%x (%d)" % (address, address))

def AIRCRAFT_ID():
	Octet1=readbyte()
	Octet2=readbyte()
	Octet3=readbyte()
	Octet4=readbyte()
	Octet5=readbyte()
	Octet6=readbyte()

	Char1 = Octet1 >> 2
	Char2 = ((Octet1<<4)& 0x3F) | (Octet2 >> 4)
	Char3 = ((Octet2<<2) & 0x3F) | (Octet3 >> 6)
	Char4 = (Octet3 & 0x3F)
	Char5 = (Octet4>>2)
	Char6 = ((Octet4<<4)& 0x3F) | (Octet5 >> 4)
	Char7 = ((Octet5<<2) & 0x3F) | (Octet6 >> 6)
	Char8 = (Octet6 & 0x3F)
	#print("%x%x%x%x%x%x" % (Octet1, Octet2, Octet3, Octet4, Octet5, Octet6))
	#print("%x%x%x%x%x%x%x%x" % (Char1, Char2, Char3,Char4, Char5, Char6,Char7,Char8))
	print("\n+---I048/240 [AIRCRAFT ID]: [%s][%s][%s][%s][%s][%s][%s][%s]" % (bin(Char1),bin(Char2),bin(Char3),bin(Char4),bin(Char5),bin(Char6),bin(Char7),bin(Char8)))  
	
	C1 = SIX_BITS_CHAR(Char1)
	C2 = SIX_BITS_CHAR(Char2)
	C3 = SIX_BITS_CHAR(Char3)
	C4 = SIX_BITS_CHAR(Char4)
	C5 = SIX_BITS_CHAR(Char5)
	C6 = SIX_BITS_CHAR(Char6)
	C7 = SIX_BITS_CHAR(Char7)
	C8 = SIX_BITS_CHAR(Char8)

	print (" 	|")
	print (" 	|____ %s%s%s%s%s%s%s%s" % (C1,C2,C3,C4,C5,C6,C7,C8))
	
	Name = C1 + C2 + C3
	for name in airline_code:
		if (name[0] == Name):
			print (" %s => %s" % (name[0],name[1]))
			
def MODE_SMB_DATA():
	print("+---I048/250 [MODE S MB DATA]")
	REP = readbyte()
	print(" |	(There Are %d MBData Blocks)" % REP)
	
	while (REP):
		MB1 = readbyte()
		MB2 = readbyte()
		MB3 = readbyte()
		MB4 = readbyte()
		MB5 = readbyte()
		MB6 = readbyte()
		MB7 = readbyte()
		print(" |____ MBdata%d: %x%x%x%x%x%x%x" % (REP, MB1,MB2,MB3,MB4,MB5,MB6,MB7))

		BDS  = readbyte()
		BDS1 = (BDS >> 4)
		BDS2 = (BDS & 0x0F)
		print("   |____ BDS%d.%d" % (BDS1,BDS2))

		REP = REP - 1

def HIEGH_3D():
	H1 = readbyte()
	H2 = readbyte()

	H = ((H1 & 0x1F) << 8) | H2

	print("+---I048/110 [HEIGHT MEASURED BY 3D RADAR]")
	if(H1 & 32):
		
		print(" |____ 3D-Height: -%d ft" % (H * 25))
	else:

		print(" |____ 3D-Height:  %d ft" % (H * 25))	



def COMM_ACAS_CAP_FLY_STAT():
	print("+---I048/230 [COMM ACAS CAPABILITY & FLIGHT STATUS]")
	C1 = readbyte()
	C2 = readbyte()

	COM = ((C1 & 0xE0) >> 5)
	if(COM == 0):
		print(" |____ COM: 000 : No Communication Capability")
	elif(COM == 1):
		print(" |____ COM: 001 : Comm_A & Comm_B Capabilities")
	elif(COM == 2):
		print(" |____ COM: 010 : Comm_A & Comm_B & UpLINK ELM")
	elif(COM == 3):
		print(" |____ COM: 011 : Comm_A & Comm_B & UpLINK & DownLINK ELM")
	elif(COM == 4):
		print(" |____ COM: 100 : Level 5 Transponder Capability")

	STAT = ((C1 & 0x1C) >> 2)
	if(STAT == 0):
		print(" |____ STAT: 000 : No Alert + No SPI + aircraft airborne")
	elif(STAT == 1): 	
		print(" |____ STAT: 001 : No Alert + No SPI + aircraft On Ground")
	elif(STAT == 2):
		print(" |____ STAT: 010 : Alert + No SPI + aircraft airborne")
	elif(STAT == 3):
		print(" |____ STAT: 011 : Alert + No SPI + aircraft on Ground")
	elif(STAT == 4):
		print(" |____ STAT: 100 : Alert + SPI + aircraft airborne OR On Ground")
	elif(STAT == 5):
		print(" |____ STAT: 101 : No Alert + SPI + aircraft airborne OR On Ground")

	if(C1 & 2):
		print(" |____ SI: 1 : SI/II Transponder Capability")
	print(" |____ bit9: Spare bit set to 0")
	
	if(C2 & 128):
		print(" |____ MSSC: 1 : Mode-S Specific Service Capability (YES)")
	else:
		print(" |____ MSSC: 0 : Mode-S Specific Service Capability (NO)")	
	if(C2 & 64):
		print(" |____ ARC : 1 : Altitude Reporting Capability (25ft Resolution)")
	else:
		print(" |____ ARC : 0 : Altitude Reporting Capability (100ft Resolution)")						
					
	if(C2 & 32):
		print(" |____ AIC : 1 : Aircraft Identification Capability (YES)")
	else:
		print(" |____ AIC : 0 : Aircraft Identification Capability (NO)")
	
	B1A = ((C2 & 0x10) >> 4)
	print(" |____ B1A : BDS1.0 bit 16 = %d" % B1A)
	
	
	B1B = C2 & 0xF
	print(" |____ B1B : BDS1.0 bits37/40 = %s" % bin(B1B))	
		 	
			
def ACAS_RES_ADV_REPORT():
	print("+---I048/260 [ACAS RESOLUTION ADVISORY REPORT]")

	AC1= readbyte()
	AC2= readbyte()
	AC3= readbyte()
	AC4= readbyte()
	AC5= readbyte()
	AC6= readbyte()
	AC7= readbyte()
	
	print(" |____ Mode S Comm B Message Data of BDS 3.0 :\n |____[%x%x%x%x%x%x%x]" % (AC1,AC2,AC3,AC4,AC5,AC6,AC7))


def MODE1_CODE_OCTAL():
	print("+---I048/055 [MODE 1 CODE OCTAL REPRESENTATION]")
	M1 = readbyte()
	if(M1 & 128):
		print(" |____ V: 1 : Code Not Validated")
	else:
		print(" |____ V: 0 : Code Validated")	
	if(M1 & 64):
		print(" |____ G: 1 : Garbled Code")
	else:
		print(" |____ G: 0 : Code Not Garbled")		

	if(M1 & 32):
		print(" |____ L: 1 : Mode-1 Code As Derived From the Reply Transponder")
	else:
		print(" |____ L: 0 : Smoothed Mode-1 Code as Provided by Local Tracker")
	Mode1_code = (M1 & 0x1F)
	print(" |____ Mode-1 Code: [%s]" % bin(Mode1_code))

def MODE1_CONF():
	print("+---I048/065 [MODE 1 CODE CONFIDENCE INDICATOR")
	CO = readbyte()
	MO1_CONF = (CO & 0x1F)
	print( "|____Mode-1 Confidence Indicator: [%s]" % bin(MO1_CONF))




# ------------------ MAIN ENTRY ---------------------------------------#

def main(argv):
	Hello = """	

     .oo .oPYo. ooooo .oPYo.  .oPYo. o  o    o        ooo.   oooooo 
    .P 8 8        8   8.      8   `8 8  `b  d'        8  `8.     d' 
   .P  8 `Yooo.   8   `boo   o8YooP' 8   `bd'         8   `8    d'  
  oPooo8     `8   8   .P      8   `b 8   .PY.   ooooo 8    8   d'   
 .P    8      8   8   8       8    8 8  .P  Y.        8   .P  d'    
.P     8 `YooP'   8   `YooP'  8    8 8 .P    Y.       8ooo'  dooooo 
..:::::..:.....:::..:::.....::..:::......::::..:::::::.....::.......
:Q29kZWQgQnkgIk9TZHogRHpheWVyIgpXaXRoIHRoZSBoZWxwIE9mIFJhb3VmCkZhY2:
::::::::::::Vib29rOiBPU2RldmR6Cg==::::::::::::::::::::::::::::::::::
	"""
	print(Hello)
	

	global f
	global index
	index = 0
	
	global total_len
	total_len = 0


	i = 1


	try:
		#print ("Hey" + sys.argv[1])
		with open(sys.argv[1], "rb") as f:

			
			#index = 0
			while(1):
				cat = readbyte()
				
				
				if (cat == 1 or cat == 48):
					
					print("\n------------------------------------------------")
					print("------------------CAT: %d-----------------------"% cat)
					print("------------------------------------------------")
					
						
				else:
					
					while ((cat != 1) and (cat != 48)):
						print("\n\n##########################################")
						print("Don't Support Cat %d" % cat)
						print("Block Data Skipped N= %d" % i)
						
						leng1 = readbyte()
						leng2 = readbyte()
					
						leng = (leng1 << 8) | leng2
						print ("+---CAT: %d" % cat)	
						print ("len is %d " % leng)
						print("##########################################\n\n")
						# Just Skip This Category Block
						leng = leng - 3 # 3 bytes of CAT and Length 
						f.seek(leng, 1)
						
						cat = readbyte()

						
						index = index - 3
						i = i + 1
				
					print("------------------------------------------------")
					print("------------------CAT: %d-----------------------"% cat)
					print("------------------------------------------------")
					#if(0)
						#print("Q29kZWQgQnkgQm91bWVuYWQgU21haW4KV2l0aCB0aGUgaGVscCBvZiBSYW91Zgo=")
					
					index = index + 1

					
				
				length1 = readbyte()
				length2 = readbyte()
				
				
				BlockData_length = (length1 << 8) | length2
				
				total_len = total_len + BlockData_length

				print ("+--- Block Len : %d" % BlockData_length)

				

				while (index < total_len):

					
					print("--------------(New Data Record)---------------")
					
					FSPEC1= readbyte()
					print("FSPEC1 : %s" % bin(FSPEC1) )
					fspec_len = 1
					if (FSPEC1 & 1):
						FSPEC2 = readbyte()	
						print("FSPEC2 : %s" % bin(FSPEC2) )
						fspec_len = fspec_len + 1
						if (FSPEC2 & 1):
							FSPEC3 = readbyte()
							print("FSPEC3 : %s" % bin(FSPEC3) )
							fspec_len = fspec_len + 1
							if (FSPEC3 & 1):
								FSPEC4 = readbyte()
								print("FSPEC4 : %s" % bin(FSPEC4) )
								fspec_len = fspec_len + 1
							else:
								print(" |____No Other FSPEC Extension")	
						else:
							print(" |____No Other FSPEC Extension")		
					else:
						print(" |____No Other FSPEC Extension")			
					print("------------------------")			
					print("FSPEC Item Has %d bytes" % fspec_len)
					print("------------------------")

					#-------------------------------- Decode Categorie 48 -----------------------------	
					if(cat == 48):
						if(FSPEC1 & 128):
							
							READ_SIC_SAC(cat)
						else:
							print("Should Have an Identifier. Inspect Where is the Problem")
							sys.exit()

						if(FSPEC1 & 64):
							TIME1 = readbyte()
							TIME2 = readbyte()
							TIME3 = readbyte()

							TIME  = (TIME1 << 16) | (TIME2 << 8) | (TIME3)

							print("+---I048/140 [Time Stamping] : %f sec" % (TIME * 1/128)) 
						
						if(FSPEC1 & 32):
							READ_DESCRIPTOR(cat)
						if(FSPEC1 & 16):
							POLAR_CORD(cat)								
						if(FSPEC1 & 8):
							MODE3_A_REPLAY_OCTAL(cat)
						if(FSPEC1 & 4):
							FLIGHT_LEVEL()
						if(FSPEC1 & 2):
							RADAR_PLOT_CHARAC(cat)
						if (FSPEC1 & 1):
							if(FSPEC2 & 128):
								AIRCRAFT_ADD()
							if(FSPEC2 & 64):
								AIRCRAFT_ID()
							if(FSPEC2 & 32):
								MODE_SMB_DATA()
							if(FSPEC2 & 16):
								TRACK_NUMBER(cat)	
							if(FSPEC2 & 8):
								CARTESIAN_CORD()
							if(FSPEC2 & 4):
								TRACK_VELOCITY(cat)
							if(FSPEC2 & 2):
								TRACK_STATUS(cat)
							if(FSPEC2 & 1):
								if(FSPEC3 & 128):
									TRACK_QUALITY(cat)
								if(FSPEC3 & 64):
									WARNING(cat)
								if(FSPEC3 & 32):
									MODE_3_CONF(cat)		
								if(FSPEC3 & 16):
									MODE_C_CODE_CONF(cat)
								if(FSPEC3 & 8):
									HIEGH_3D()
								if(FSPEC3 & 4):
									RADIAL_DOPPLER_SPEED(cat)
								if(FSPEC3 & 2):
									COMM_ACAS_CAP_FLY_STAT()
								if(FSPEC3 & 1):
									if(FSPEC4 & 128):
										ACAS_RES_ADV_REPORT()
									if(FSPEC4 & 64):
										MODE1_CODE_OCTAL()
									if(FSPEC4 & 32):
										MODE_2_CODE(cat)
									if(FSPEC4 & 16):
										MODE1_CONF()
									if(FSPEC4 & 8):
										MODE_2_IND(cat)
									if(FSPEC4 & 4):
										SP_DATA = readbyte()
										print("SP data: %d" % SP_DATA)
										if(SP_DATA & 128 ):
											SP_DATA_EXT1 = readbyte()
											print("SP data EXT 1: %d" % SP_DATA_EXT1)
											if(SP_DATA_EXT1 & 128):
												SP_DATA_EXT2 = readbyte()
												print("SP data EXT 2: %d" % SP_DATA_EXT2)
									if(FSPEC4 & 2):
										RE_DATA = readbyte()
										print("RE data: %d" % RE_DATA)
										if(RE_DATA & 128 ):
											RE_DATA_EXT1 = readbyte()
											print("RE data EXT 1: %d" % RE_DATA_EXT1)
											if(RE_DATA_EXT1 & 128):
												RE_DATA_EXT2 = readbyte()
												print("RE data EXT 2: %d" % RE_DATA_EXT2)			

					# Decode CAT 001								

					elif (cat == 1):

						#FSPEC1

						if(FSPEC1 & 128):
							
							READ_SIC_SAC(cat)
						else:
							print("Should Have an Identifier. Inspect Where is the Problem")
							sys.exit()

						if(FSPEC1 & 64):
							READ_DESCRIPTOR(cat)
						
						if(FSPEC1 & 32):
							if(track):
								TRACK_NUMBER(cat)
							else:
								print ("Plot :")
								POLAR_CORD(cat)
						
						if(FSPEC1 & 16)	:
							if(track):
								print ("Track :")
								POLAR_CORD(cat)

							else:
								print ("Plot :")
								MODE3_A_REPLAY_OCTAL(cat)

						if(FSPEC1 & 8):
							if(track):
								print ("Track :")
								CARTESIAN_CORD()
							else:
								print ("Plot :")
								MODE_C_BINARY()

						if(FSPEC1 & 4):
							if(track):
								print ("Track :")
								TRACK_VELOCITY(cat)
							else:
								print("Plot :")
								RADAR_PLOT_CHARAC(cat)

						if(FSPEC1 & 2):
							if(track):
								print ("Track :")
								MODE3_A_REPLAY_OCTAL(cat)
							else:
								print ("Plot :")
								TRUNCATED_TIME()

					 	if (FSPEC1 & 1):

						#FSPEC 2 		
					 		if(FSPEC2 & 128):
					 			if(track):
					 				print ("Track :")
					 				MODE_C_BINARY()
								else:
									print ("Plot :")
									MODE_2_CODE(cat)
							if(FSPEC2 & 64):
					 			if (track):
					 				print ("Track :")
					 				TRUNCATED_TIME()
					 			else:
					 				print ("Plot :")
					 				RADIAL_DOPPLER_SPEED(cat)		
							if(FSPEC2 & 32):
								if(track):
									print ("Track :")
									RADAR_PLOT_CHARAC(cat)
								else:
									print ("Plot :")
									RECIEVED_POWER()	
							if(FSPEC2 & 16):
								if(track):
									print ("Track :")
									RECEIVED_POWER()
								else:
									print ("Plot :")
									MODE_3_CONF(cat)
							if(FSPEC2 & 8):
								if(track):
									print ("Track :")
									RADIAL_DOPPLER_SPEED(cat)
								else:
									print ("Plot :")
									MODE_C_CODE_CONF(cat)	
							if(FSPEC2 & 4):
								if(track):
									print ("Track :")
									TRACK_STATUS(cat)
								else:
									print ("Plot :")
									MODE_2_CONF()
							if(FSPEC2 & 2):
								if(track):
									print ("Track :")
									TRACK_QUALITY(cat)
								else:
									print ("Plot :")
									WARNING(cat)
						# FSPEC3
							if(FSPEC2 & 1):
								if(FSPEC3 & 128):

									if(track):
										print ("Track :")
										MODE_2_CODE(cat)			
									else:
										print ("Plot :")
										X_PULSE()
								
								if(FSPEC3 & 64):
									if(track):
										print ("Track :")
										MODE_3_CONF(cat)
									else:
										print ("Plot :")
										print("Just Empty For Plot Infos.")	
								if(FSPEC3 & 32):
									if(track):
										print ("Track :")
										MODE_C_CODE_CONF(cat)
									else:
										print ("Plot :")
										print("Just Empty For Plot Infos.")		
								if(FSPEC3 & 16):

									if(track):
										print ("Track :")
										MODE_2_IND(cat)
									else:
										print ("Plot :")
										print("Just Empty For Plot Infos.")		
								if (FSPEC3 & 8):
									if(track):
										print ("Track :")
										WARNING(cat)
									else:
										print ("Plot :")
										print("Just Empty For Plot Infos.")		
									
								if (track):
									print ("Track :")		
									if (FSPEC3 & 1):
										X_PULSE()
	
	except EnvironmentError:
		print("<"+sys.argv[1]+">" + " file Does not exist")								

if __name__ == "__main__":
   main(sys.argv[1:])							



