---
title: "42. Služby aplikační vrstvy (web, e-mail, DNS, IP telefonie, správa SNMP, Netflow)"
category: okruh
okruh: 42
tags: [networking, web]
aliases: [aplikační vrstva, HTTP, DNS, SMTP, POP3, IMAP, VoIP, SIP, RTP, SNMP, NetFlow, URL]
relationships:
  - target: "[[topics/43-tcp-ip-komunikace]]"
    type: uses
  - target: "[[topics/37-webova-rozhrani-autentizace]]"
    type: related_to
sources: ["_sources/docx/szz-42.docx"]
summary: Protokoly aplikační vrstvy (nad TCP/UDP) — web (HTTP, URL), e-mail (SMTP/POP3/IMAP, MUA/MTA/MDA), DNS (rezoluce, typy záznamů), IP telefonie (SIP/RTP), správa sítě (SNMP, NetFlow).
provenance:
  extracted: 0.91
  inferred: 0.07
  ambiguous: 0.02
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-06-03
tier: supporting
created: 2026-06-03T18:45:00Z
updated: 2026-06-03T18:45:00Z
---

# 42. Služby aplikační vrstvy

> SZZ okruh 42 (FIT BUT). Protokoly, které používají koncové aplikace.

## Shrnutí

### Aplikační vrstva a protokoly
- Nejvyšší vrstva; aplikace si komunikaci zajišťuje sama (ne OS) přes **standardizované protokoly**.
- Nad **UDP**: DNS, TFTP, SNMP, NetFlow, NTP, SIP, RTP. Nad **TCP**: HTTP, SMTP, FTP, POP3, IMAP, LDAP.

### Web a DNS
- **HTTP** — klient-server, **bezstavový** (stav přes cookies); request (metoda GET/POST/PUT/PATCH/DELETE + hlavičky + tělo) / response (status kód 1xx–5xx). **URL** = podmnožina URI (jak a kde zdroj získat).
- **DNS** — překlad doménových jmen na IP (rezoluce); hierarchie (kořen → TLD → 2. řád); UDP/53; záznamy **A, AAAA, MX, CNAME, SRV**; rekurzivní/autoritativní/cache servery.

### E-mail
- **MUA** (klient) → **MTA** (server, doručuje dle obálky a **MX** záznamu) → **MDA** (lokální doručení).
- **SMTP** (odesílání, port 25) × **POP3** (stahuje a maže, port 110) × **IMAP** (ponechává na serveru, synchronizuje, port 143).
- Kódování 8-bit → 7-bit ASCII (**Base64**, Quoted-printable); zabezpečení obsahu **PGP**, S/MIME.

### IP telefonie a správa sítě
- **VoIP**: **SIP** (signalizace — REGISTER/INVITE/ACK), **RTP** (přenos médií přes UDP, mimo SIP proxy).
- **SNMP** (správa zařízení; agent/manager; GET/SET/TRAP; UDP 161/162), **NetFlow** (toky — exportér/kolektor, detekce útoků).

Transportní protokoly viz [[topics/43-tcp-ip-komunikace]]; webová rozhraní a session viz [[topics/37-webova-rozhrani-autentizace]]; zabezpečení viz [[topics/44-smerovani-zabezpeceni-siti]].

## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**HTTP a web** ↪ [[#Web a DNS]]
- *GET vs. POST?* → GET získává zdroj (bez modifikace), POST odesílá data / vytváří zdroj.
- *Stavové kódy?* → 2xx úspěch, 3xx přesměrování, 4xx chyba klienta (404), 5xx chyba serveru.
- *URL vs. URI vs. URN?* → URL (kde + jak získat) a URN (jen identifikace) jsou podmnožiny URI.

**DNS** ↪ [[#Web a DNS]]
- *K čemu DNS, jak funguje?* → Překlad jména na IP (rezoluce); hierarchie root → TLD → domény; UDP/53.
- *Typy záznamů?* → A/AAAA (IP), MX (mail), CNAME (alias), SRV (služba).

**E-mail** ↪ [[#E-mail]]
- *SMTP vs. POP3 vs. IMAP?* → SMTP odesílá; POP3 stahuje a maže ze serveru; IMAP ponechává a synchronizuje (více zařízení).
- *MUA/MTA/MDA?* → klient / přenosový server (dle MX) / lokální doručovatel.

**Správa sítě** ↪ [[#IP telefonie a správa sítě]]
- *NetFlow — tok?* → Posloupnost paketů se společnými atributy; exportér posílá, kolektor sbírá (detekce DDoS).
- *SNMP?* → Správa zařízení (agent/manager, GET/SET/TRAP, UDP 161/162).

## Plné znění (ke studiu)

V modelu TCP/IP i v modelu ISO/OSI je aplikační vrstva poslední. Referenční model ISO/OSI předpokládá, že jednotlivé aplikace budou mít některé společné rysy, které se vyplatí realizovat samostatně a implementovat jen jednou. TCP/IP model vznikal více z praktických zkušeností. Předpokládá, že jednotlivé aplikace nebudou mít tolik společného, aby se tyto části vyplatilo osamostatnit. TCP/IP na rozdíl od referenčního ISO/OSI modelu očekává, že každá aplikace si sama zajistí to, co potřebuje a co jí nenabízí nižší vrstvy.

Na rozdíl od nižších vrstev (transportní, síťová a vrstva síťového rozhraní) není komunikace na aplikační vrstvě zajištěna OS (sockets) či HW počítače. **Každá aplikace si musí komunikaci na této vrstvě zajišťovat sama.** Proto, aby se nelišily způsoby komunikace aplikace od aplikace, používají se na aplikační vrstvě (stejně jako na jiných) **standardizované protokoly**. Protokol, který aplikace pro komunikaci používá, určuje její změření.

Na základě požadavků aplikace může být aplikační protokol implementován nad UDP (rychlejší, ztrátový), nebo nad TCP (pomalejší, bezztrátový), příklady protokolů:
![[media/szz-42/media/image20.png]]

- **UDP**: **DNS** (překlad doménových jmen na IP adresy), **TFTP** (přenos souborů), **SNMP** (správa sítě), **Netflow** (správa sítě), **NTP** (synchronizace času), **SIP** (signalizace VoIP), **RTP** (přenos zvuku a obrazu), **RTCP** (řídící informace pro RTP a QoS),
- **TCP**: **HTTP** (webové stránky), **SMTP** (e-mailová komunikace), **LDAP** (adresářové služby, může být i přes UDP), **FTP** (přenos souborů), **POP3** (stahování el. pošty), **IMAP** (stahování a čtení el. pošty).
![[media/szz-42/media/image13.png]]

### Adresa

**Způsob identifikace adresáta pomocí jednoznačné informace**.

## Web (HTTP)

**World Wide Web** (také jen web) je tvořen aplikacemi, které běží na protokolu **http** (Hypertext Transfer Protocol), respektive jeho šifrované verzi **https** (Hypertext Transfer Protocol Secure). WWW je systém pro **prohlížení**, **ukládání** a **odkazování dokumentů** nacházejících se **na internetu**. Dokumenty (webové stránky) jsou uloženy na **webových serverech** a přistupujeme k nim pomocí **webového prohlížeče**. Navzájem jsou propojeny pomocí **hypertextových odkazů** zapisovaných ve formě **URL**.

### URI, URL a URN

URL a URN jsou podmnožinou **URI** (Uniform Resource Identifier). URI je textový řetězec s definovanou strukturou, který slouží k **přesné specifikaci zdroje** informací.

- **Uniform Resource Name** (URN): jasně identifikuje zdroj, ale neřeší jeho dostupnost. Schema URN je \<URN\> ::= "urn:" \<NID\> ":" \<NSS\>, např. urn:isbn:0451450523.
- **Uniform Resource Locator** (URL): určuje, kde je identifikovaný zdroj dostupný a mechanismus pro jeho získávání. **Adresa** URL definuje, **jak** lze **zdroj** **získat**. Nejobecněji má URL tvar \<scheme\>:\<scheme-specific-part\>, konkrétněji pak protokol://server.doména2.doména1:port/cesta/název?dotaz#kotva.

Pro adresaci (jako **adresu**) na webu **používáme URL**, i když v HTTP RFC je to zobecněno na URI (ale pomocí URN zdroj na internetu nenajdeme).

### HTTP

HTTP je protokol typu **klient-server**, což znamená, že požadavky **iniciuje příjemce** (klient), obvykle webový prohlížeč. Klienti a servery komunikují výměnou jednotlivých zpráv (na rozdíl od proudu dat). Klient zasílá požadavky/dotazy (**request**) a server na ně odpovídá odpovědí (**response**). Jedná se o **bezstavový** protokol, tj. že není zachována návaznost jednotlivých dotazů a odpovědí (řeší se ale pomocí **Cookies**).

#### **Schéma HTTP dotazu**

\<metoda\> \<cesta\> \<verze protokolu\>CRLF \<hlavička 1\>CRLF \<hlavička 2\>CRLF \<hlavička…\>CRLF \<hlavička n\>CRLF CRLF \<tělo dotazu\>

- **metoda** je:
![[media/szz-42/media/image5.png]]

  - **GET** - získání zdroje/dat (nemělo by se pomocí GET nikdy modifikovat),
  - **POST** - odeslání dat na server, mělo by znamenat vytvoření nového zdroje,
  - **PATCH** - částečná úprava zdroje,
  - **PUT** - změna aktuálního zdroje s daty v těle dotazu,
  - **DELETE** - smazání zdroje,
  - aj. (**HEAD**, **CONNECT**, **TRACE, …**).
- **cesta** specifikuje umístění zdroje na serveru,
- **verze protokolu** je např. **HTTP/1.1**,
- **hlavičky** jsou ve tvaru název:hodnota, nejdůležitější hlavičkou je hlavička Host, která specifikuje adresu serveru.
- **tělo** dotazu je tvořeno daty, které odesíláme na server, může jít o JSON, HTML, XML, binární data, … specifikováno pomocí hlavičky **Content-Type** a **MIME** typu dat (application/json, text/html, application/xml).

#### **Schéma HTTP odpovědi**

\<protocol version\> \<status code\> \<status message\>CRLF \<hlavička 1\>CRLF \<hlavička 2\>CRLF \<hlavička…\>CRLF \<hlavička n\>CRLF CRLF \<tělo dotazu\>

- **protocol version** je např. **HTTP/1.1**,
![[media/szz-42/media/image25.png]]

- **status code** je jeden ze skupiny:
  - **100-199**: **informační** odpověď,
  - **200-299**: odpověď hlásící **úspěch**,
  - **300-399**: odpověď hlásící **přesměrování**,
  - **400-499**: odpověď hlásící **chybu na straně klienta**,
  - **500-599**: odpověď hlásící **chybu na straně serveru**.
- **status message** dále upřesňuje status code, např.:
  - 200 OK,
  - 201 created,
  - 202 updated,
  - 400 bad request,
  - 401 unauthorized,
  - 403 forbidden,
  - 404 not found,
![[media/szz-42/media/image17.png]]

## E-mail

Email je mechanismus pro zasílání elektronické pošty. Je tvořen:

- **obálkou** - tu vytváří poštovní **server** (MTA - Mail Transfer Agent) a obsahuje:
  - MAIL FROM:\<odesilatel@domena.com\>
  - RCPT TO:\<prijemce@domena.com\>
- **hlavičkou** - vytváří poštovní **klient** (MUA - Mail User Agent), má tvar \<název\>:\<hodnota\> a může obsahovat (mimo jiné):
  - From, To, Subject, Cc, Bcc, Date, Return-Path, Received, …
- **tělem** - vytváří poštovní klient a obsahuje **7-bit ASCII** data (původně, hlavička a obálka jsou také 7-bit), dnes rozšíření **MIME** (Multipurpose Internet Mail Extensions – umožňují zasílat text v jiných formátech než jen ASCII a také posílat přilohy v podobě obrázků, audia, videa či binárních dat).

K identifikaci adresáta (**adresa**) se u emailu používá **emailová adresa**.

### Kódování

V případě emailu se jedná o **převod** binárních nebo jiných **8-bit** znaků na **7-bit ASCII** znaky. Rozhodně se **nejedná o šifrování**.

#### **Quoted-printable**

Nahrazují se pouze 8-bit znaky a převádějí se na **3 znaky**, a to rovnítko a 2 **hexadecimální znaky** (reprezentují index v 8-bit poli znaků), např. =F9 nebo =B9. Rovnítko musí být také kódováno jako (=3D). Teoreticky může dojít k prodloužení textu až o **200%**. Prakticky se používá při **kódování textu** (jazyka, např. čj; zůstává částečně čitelné), kde může mít menší prodloužení než **Base64** (záleží také na národní abecedě), **nevhodné pro** **binární data**.

#### **Base64**

Kódují se vždy všechny znaky, a to po trojicích. **Trojice 8-bit** znaků je převedena na **čtveřici 6-bit** znaků (3\*8 == 4\*6). Šestibitové znaky jsou následně převáděny na 7-bitové indexací do pole: **ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/**. Chybějící znaky do čtveřice jsou doplňovány pomocí rovnítka. Text je vždy prodloužen o **33%**, kódování je **vhodné pro binární data**.

### Simple Mail Transfer Protocol (SMTP)

Aplikační protokol nad TCP pro **posílání pošty** na portu **25**. S protokolem SMTP pracují 3 programy:

- **MUA – Mail User Agent**: poštovní klient, který zpracovává zprávy u uživatele.
- **MTA – Mail Transfer Agent**: server, který se stará o doručování zprávy na cílový systém adresáta. Ignoruje hlavičku a tělo zprávy, pro doručování **používá pouze obálku** (analogie s poštou).
- **MDA – Mail Delivery Agent**, program pro lokální doručování, který umísťuje zprávy do uživatelských schránek, případně je může přímo automaticky zpracovávat (ukládat přílohy, odpovídat, spouštět různé aplikace pro zpracování apod.).

Pro vyhledání serveru adresáta, na který má být předána zpráva, vyhledává MTA záznam **MX** v **DNS**. Dotaz na DNS obsahuje **doménové jméno** za znakem ‘@’, DNS vrací **doménové jméno** SMTP serveru adresáta. Toto doménové jméno je pak dotazem na A/AAAA záznam přeloženo na IP adresu adresáta. Neexistuje RFC standard zakazující mít v MX přímo IP adresu adresáta, ale typicky se to nedělá a nedoporučuje (prevence před spamem aj.)

#### **SMTP příkazy**

HELO, HELP, MAIL FROM, RCPT TO, RSET, QUIT, …

### Post Office Protocol (POP3)

Protokol sloužící pro stahování elektronické pošty přes TCP port 110. Protokol je mnohem **jednodušší** než IMAP a umožňuje především **stahovat** poštu ze serveru (a zobrazovat počet příchozích zpráv). Po stáhnutí je pošta ze serveru **implicitně smazána** (může být nastaveno jinak, třeba po určité době bude pošta smazána). Implicitní mazání neumožňuje mít jednu schránku na více zařízeních a i pokud je nastaveno jinak, není protokol vhodný pro více schránek (např. přesun zpráv, označení zpráv atd. se děje pouze lokálně, na serveru se nic nemění). Protokol je vhodný, pokud na serveru máme **málo místa** (Poté, co si uživatel zprávy stáhne, server bude opět prázdný a může přijímat další zprávy. V podstatě se jedná o princip poštovní schránky. Když bychom ze schránky u domu nevyndávali poštu, časem by se schránka zaplnila a další pošta by se tam už nedala dát. Naopak, když pravidelně poštu ze schránky vyndáváme, stačí nám malinkatá schránka na roky přijímání pošty. To na IMAP bez manuálního mazání pošty ze serveru neuděláme.).

### Internet Mail Access Protocol (IMAP)

Protokol sloužící pro **prohlížení** a stahování elektronické pošty přes TCP port 143. Pomocí protokolu se navazuje s emailovým serverem trvalé spojení. Zprávy není nutné stahovat celé, stačí pouze základní informace (hlavičky zpráv). Zpráva je ze serveru stažena celá, až když ji chce uživatel na klientovi číst (poté může být zase smazána). Na **serveru zprávy zůstávají neustále**, dokud je uživatel explicitně nesmaže. IMAP **reflektuje změny** provedeny uživatelem v klientovi **na server** (např. označení zprávy za přečtenou, přesun zprávy do jiné složky, přidání/odebrání štítku atd.). Je proto **vhodný při přístupu z více klientů** (zařízení), změny provedené na jednom klientovi jsou synchronizovány na druhý.

### Pretty Good Privacy (PGP)

Protokol SMTP a IMAP lze přenášet zabezpečeně přes internet (pomocí SSL, TLS, HTTPS). Zmíněné protokoly ale **nezabezpečují obsah zprávy**, ta zůstává na emailovém serveru v čitelné formě. Zabezpečit tělo zprávy lze např. pomocí **PGP**. **PGP** zajišťuje:

- **integritu dat**,
- **autentizaci odesílatele**,
- **šifrování (důvěrnost)**.

Postup zabezpečení:

1. Odesílatel vypočte **heš** zprávy a svým privátním klíčem ji **podepíše**.
2. **Komprimuje** obsah zprávy.
3. **Zašifruje** obsah zprávy vygenerovaným symetrickým klíčem.
4. Symetrický klíč **zašifruje veřejným** klíčem příjemce (dešifrovat může pouze příjemce svým privátním) a připojí jej k zašifrované zprávě.
5. Převede obsah do **Base64** (v mailu mohou být pouze 7-bit znaky, viz výše).

### Secure/Multipurpose Internet Mail Extensions (S/MIME)

Další možnost zabezpečení obsahu emailu založená na **asymetrické kryptografii** a **digitálních podpisech**.

## Domain Name System (DNS)

DNS je **globální decentralizovaný adresář** názvů počítačů a dalších identifikátorů síťových zařízení a služeb. Hlavní funkcí DNS je **překlad doménových jmen na IP adresy**. DNS rozděluje globální prostor doménových adres (jmen) **hierarchicky**, což umožňuje delegaci. Záznamy jsou uloženy na třech typech serverů, a to **primární**, **sekundární** a **záložní**. Princip vyhledávání v DNS se nazývá **rezoluce**. Protokol DNS pro rezoluci používá primárně UDP, port 53. TCP lze použít při přenosu většího množství dat, např. při přenosu DNS **zón**.

### Prostor doménových jmen

Hierarchické uspořádání DNS záznamů do stromové struktury.

- **Kořenovou doménu** “.” má na starost organizace **ICANN**.
- **Top Level Domain** - TLD (domény 1. řádu): zprávu těchto domén deleguje ICANN na další organizace, v ČR je to CZ.NIC. Jde o domény (.cz, .com, .eu, .org, .net, …).
- Domény 2. a nižších řádů: tyto domény spravují konkrétní organizace. Např. u CZ.NIC si může každý zakoupit doménu \*.cz (\* je název 2. řádu) a poté ji spravovat a případně prodávat domény \*.\*.cz. Jde o domény (seznam.cz, vut.cz, google.com, …)

> Zdroj obrázku: [<u>https://raventools.com/marketing-glossary/root-domain/</u>](https://raventools.com/marketing-glossary/root-domain/)
![[media/szz-42/media/image1.png]]

#### **Reverzní mapování**

Umožňuje na základě **IP** adresy vyhledat doménové jméno. Reverzní mapování zajišťují 2 podstromy **in-addr.arpa.** pro IPv4 a **ip6.arpa.** pro IPv6. Pro IPv4 adresy se zapisuje běžným zápisem ale **zprava doleva**. U IPv6 se každá hexadecimální číslice odděluje tečkou, zápis je také **zprava doleva**.

- **IPv4**: 147.28.29.30 → **30.29.28.147.in-addr.arpa.**
- **IPv6**: 2001:db8::567:89ab → **b.a.9.8.7.6.5.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa.**

### Záznamy DNS

Existuje velké množství DNS záznamů, zde jsou ty nejdůležitější:

- **SOA**: zahajuje záznam zónového souboru, každá zóna má **právě jeden** záznam SOA. Obsahuje mimo jiné název primárního DNS serveru a emailovou adresu správce.

![[media/szz-42/media/image8.png]]

- **NS**: určuje **autoritativní** server pro danou doménu.
![[media/szz-42/media/image19.png]]

- **A**: přímé mapování doménového jména na IPv4 adresu.

![[media/szz-42/media/image24.png]]

- **AAAA**: přímé mapování doménového jména na IPv6 adresu.

![[media/szz-42/media/image28.png]]

- **MX**: Slouží pro zjištění doménového jména poštovního serveru, může obsahovat více záznamů rozlišených prioritou (menší číslo značí vyšší prioritu).

![[media/szz-42/media/image11.png]]

- **CNAME**: slouží jako alias, mapuje jej na jméno počítače (síťového zařízení), aliasy nesmí být na pravé straně záznamů a PC jich může mít více.

![[media/szz-42/media/image31.png]]

- **PTR**: mapuje IPv4 nebo IPv6 adresu na doménovou adresu, obsahuje **reverzní** mapování. Využívají speciální podstromy **in-addr.arpa.** pro IPv4 a **ip6.arpa.** pro IPv6.
![[media/szz-42/media/image23.png]]

<!-- -->

- **SRV**: slouží k lokalizaci služeb a serverů, např. SIP. Mají tvar \_service.\_protocol.domain_name.

![[media/szz-42/media/image7.png]]

- a další, dohromady asi 91 DNS záznamů.

#### **Přehled DNS záznamů**
![[media/szz-42/media/image16.png]]

### DNS rezoluce

Jedná se o proces vyhledání odpovědi v systému DNS. Komunikace DNS je typu klient-server. Dotazy aplikací (klientů) vyřizuje systémová rutina OS tzv. DNS resolver (protože OS může některé DNS záznamy mít ve VP a také aby to každá aplikace nemusela implementovat). Využívá stromovou strukturu jmen a kořenové DNS servery (těch je 13 a obsahují kořenovou zónu). Používají se dva způsoby rezoluce: rekurzivní a iterativní. Pro to, aby počítač mohl provést DNS rezoluci, musí nejdříve znát IP adresu lokálního DNS serveru / resolveru. Ta může být zadána buď ručně (staticky) nebo jí získá od **DHCP** (IPv4) serveru (ten přiděluje: **IP adresu**, **masku sítě**, **implicitní bránu** (default gateway) a **adresu DNS serveru**). Adresu **IPv6 DNS** serveru lze získat pomocí **Router Solicitation** zprávy a odpovědi **Router Advertisement** (ICMPv6), která mimo jiné může vracet IP adresu DNS serveru.

#### **Rekurzivní dotaz**

Rekurzivní dotaz provádí **rekurzivní** server, který po dotazu vždy **vrátí IP** adresu (pokud existuje). Při dotazu na rekurzivní server mohou nastat tyto situace:

- rekurzivní server **zná** doménové jméno (má ho v zónovém souboru nebo v cache) a vrátí ho klientovi,
- rekurzivní **nezná** doménové jméno a dotazuje se jiného DNS serveru (pokud nezná žádnou část doménového jména, tak je to **kořenový server -** zjistí ze zóny **hint** (součást instalace), jinak může volat autoritativní server pro danou část doménového jména, např. při dotazu na **stud.fit.vutbr.cz.** zná již **vutbr.cz.**, tak se ptá tam), jiný DNS server může být:
  - **rekurzivní,** který vrací přímo **IP** (a dotazující se server si ji může uložit do cache),
  - **iterativní**, který buď vrací **IP**, pokud ji zná, nebo vrací **NS** záznam serveru, který ji může znát. **Rekurzivní** DNS server poté musí sám kontaktovat tento server.

Rekurzivní servery jsou většinou pouze servery nejblíž počítačum (klientů) poskytované od **ISP**.

- **výhody**: rychlejší než iterativní DNS servery, protože si v průběhu rezoluce mohou ukládat výsledek do cache a ten příště ihned zprostředkovat.
- **nevýhody**: bezpečnostní rizika, možnosti útoku jako **cache poisoning** nebo **DNS amplification attack** (DDoS viz [<u>https://www.cisa.gov/uscert/ncas/alerts/TA13-088A</u>](https://www.cisa.gov/uscert/ncas/alerts/TA13-088A))

#### **Iterativní dotaz**

Iterativní dotaz provádí **iterativní server**, který po dotazu vrátí nejlepší možnou odpověď, a to:

- **zná** mapování doménového jména na IP adresu, tedy ji vrátí.
- **nezná** mapování na IP adresu,
  - ale **zná DNS server**, který ji může znát (tento server je na cestě od kořene DNS stromu k hledanému uzlu), a vrací **NS** záznam (doménové jméno autoritativního DNS serveru) tohoto serveru,
  - **nezná** ani žádný **DNS server**, který by ji mohl znát, a vrací NS záznam kořenového DNS serveru.

> Dotazující se (klient nebo rekurzivní server) poté musí rezoluci opakovat s takto získaným **NS** záznamem.

#### **Obrázek rekurzivního i iterativního dotazu**

![[media/szz-42/media/image10.png]]

### Přenos zón

Mechanismus, který umožňuje kopírovat zónové soubory z primárních DNS serverů na sekundární pro zvýšení rychlosti DNS rezoluce, zlepšení distribuce a rozdělení zátěže. Sekundární server musí aktualizovat zónové soubory dle intervalu specifikovaném v záznamu **SOA** (DNS polling). Existují dva způsoby přenosu zón, oba jsou realizované přes **TCP** (DNS rezoluce je přes UDP).

- **Celkový přenos zón** (AXFR): primární server posílá po vyžádání sekundárním serverem celý zónový soubor.
- **Přírůstkový přenos zón** (IXFR): sekundární server posílá s výzvou o přenos záznam SOA, pro který chce zónový soubor. Primární server zkontroluje, k jakým došlo změnám, a odesílá pouze záznamy, která byly změněny.

Případně může primární server notifikovat (**DNS notify**) sekundární servery o změně zóny a ty si ji poté aktualizují. Pak je zajištěno, že i sekundární servery mají vždy **aktuální** záznamy.

### Druhy DNS serverů

- **Primární**: poskytují vždy autoritativní odpověď pro daný SOA záznam, pro každou doménu je vždy **pouze jeden primární** server.
- **Sekundární**: získávají primární zónové soubory od primárních serverů, slouží jako záloha, poskytuje také autoritativní odpověď, protože má **celý zónový soubor** pro daný SOA záznam (tedy pro danou zónu).
- **záložní/cache**: Pouze přijímá dotazy, které předává dalším DNS serverům a ukládá si odpovědi do VP. Pokud má uloženou odpověď ve VP, může jí vrátit při rezoluci, tato odpověď je ale **neautoritativní**. Záznamy z VP jsou po určitém čase (uvedeno v záznamu od primárního/sekundárního serveru) odstraňovány/aktualizovány.

Každý server může být **současně** primární, sekundární i záložní. Každou funkci ale plní pro jiné domény.

### Struktura DNS zprávy

![[media/szz-42/media/image29.png]]

Provádět DNS rezoluci můžeme např. pomocí nástrojů **nslookup**, **dig** a **host**.

### Struktura DNS záznamů

![[media/szz-42/media/image21.png]]

### Bezpečnost DNS

Jedná se o veřejnou a nešifrovanou službu, která může být terčem útoků. Mezi útoky patří:

- **podvržení odpovědi**: Útočník zašle neautorizovanou odpověď na dotaz klienta před tím, než to stihne DNS server. Útočník hádá ID odpovědi. Tento útok vede na to, že klient obdrží nesprávnou IP a v případě např. http stránek může na této adrese existovat identická stránka (např. internetové bankovnictví), která je ale ovládaná útočníkem.
- **cache poisoning**: vložení nesprávné informace pro mapování DNS záznamů do VP záložních serverů (ty pak poskytují špatné adresy při rezoluci a nastává problém viz předešlý bod). Využívá se k tomuto útoku sekce **Additional**.
- (Distributed) **Denial of Service** ((D)DoS): Snaho o přetížení DNS serveru, které zamezuje poskytovat odpovědi na legitimní dotazy. Dnes je distribuce DNS tak vysoká, že tento útok je prakticky nereálný.

#### **Zajištění integrity a autentizace DNS záznamů**

Zajištění těchto dvou vlastností **chrání** před útokem **podvržením** i před **cache poisoning**. Zajišťujeme je pomocí **DNSSEC** - mechanismus, který používá **asymetrickou kryptografii** a **podepisování DNS** **záznamů** a **klíčů**. Pro implementaci **DNSSEC** se využívají další DNS záznamy:

- **DNSKEY**: veřejný klíč pro ověřování podpisů,
- **RRSIG**: podpis daného záznamu (podepsán soukromým klíčem),
- **NSEC**, **NSEC3**: odkaz na další záznam při dotazu na neexistující doménu.
- **DS**: záznam s veřejným klíčem pro ověření záznamu **DNSKEY**, uložen v nadřazené doméně.

#### **Řetězec důvěry (chain of trust)**

Implementace zajištění **autentizace** a **integrity dat** DNS záznamů (implementace DNSSEC). Pro vytvoření řetězce důvěry se používají dva klíče (respektive 4 každý klíč tvoří dvojice **soukromý**/**veřejný**):

- **Zone Signing Key (ZSK)**: slouží k podpisu dat **privátním** klíčem, která DNS server poskytuje v odpovědích. **Veřejný** klíč pro dešifrování odpovědi je poté uložen (a podepsán KSK) na dotazovaném serveru.
- **Key Signing Key (KSK)**: privátní klíč slouží pro podepsání ZSK, veřejný je uložen na serveru rodičovské domény. Resolver tak může **validovat pravost** ZSK.

Princip **řetězce důvěry** je založen na **rekurzivním podpisu** klíčů. Kořenové servery mají **veřejně známé** **KSK** (není je třeba ověřovat), kterými podepisují své **ZSK**. Pomocí **ZSK** kořenových serverů jsou pak podepsány záznamy **DS** (a ostatní) obsahující **KSK** domén **1. řádu** (TLD). Domény **1. řádu** pak tímto **KSK** podepíší svůj **ZSK** a tím podepisují záznamy ze svého zónového souboru, které obsahují také **DS** záznamy s **KSK** domén **2. řádu**… a takhle to jde až k listům doménového stromu.

#### **Šifrování provozu DNS**

**Autentizaci** a **integritu** dat lze ještě rozšířit o **šifrování** záznamů. To je realizováno pomocí **DNS over TLS** (DoT) a **DNS over HTTPS** (DoH). Oba vyžadují **TCP**. DNS dotazy jsou tak viditelné pouze klientovi a danému dotazovanému serveru. Řeší to sice problém s odposloucháváním, ale **neřeší to problém soukromí**. Server, na který se dotazujeme (např. Google) pořád **má přehled** o tom, co navštěvujeme a může to tak využít např. pro reklamy.

## IP telefonie

Také známá pod zkratkou VoIP (Voice over IP). IP telefonie implementuje způsob komunikace (tj. primárně telefonní hovory), která je normálně běžná pro sítě s **přepojováním okruhů** - **Public Switched Telephone Network** (PSTN). PSTN je tvořena:

- koncovými zařízeními (telefony), které jsou připojeny k **Private Branch Exchange** (PBX).
- lokální smyčkou (spoj mezi PBX a ústřednou (Central office),
- ústřednami (realizuje spojení s další ústřednou),
- páteřními spoji (trunks), které spojují ústředny.

Telefonní hovory pomocí **PSTN** se vyznačují:
![[media/szz-42/media/image14.png]]

- **garantováním šířky pásma** a spolehlivého přenosu,
- **dobrou kvalitou** přenosu u digitálních ústředen,
- **napájením koncových zařízení** (telefony fungují, i když vypadne proud – nesmí však současně vypadnout i v ústředně),
- **spolehlivostí a bezchybností**, které jsou zajištěny dedikovanými spoji.

Stejné **požadavky** jsou tak očekávány **i u IP telefonie** na paketových sítích. Některé požadavky ale mohou být těžce realizovatelné, např, zajištění dostatečného přenosového pásma (jeho garance) a s tím související kvalita hlasu (i když dnes to již se stoupající rychlostí internetu není problém) nebo zajištění napájení telefonů (nutnost použití záložních zdrojů). Dále je po IP telefonech požadována **integrace s veřejnou PSTN** a **mobilními sítěmi**.

### Architektura IP telefonie

Architektura IP telefonie je tvořena několika zařízeními:

- **DHCP server** - přiděluje IP adresu telefonům a ostatním zařízením, umožňuje získat adresu DNS serveru,
- **DNS server** - provádí překlad **tel. čísel** a **sip URI** na IP adresy,
- **Ústředna** (Call Server/Gatekeeper) - zajišťuje registraci VoIP zařízení, které pak lze vytáčet,
- **IP telefon** (IP phone) - může se jednat o tzv. **soft phone** tj. softwarový telefon, nebo normální telefon připojený k internetu,
- **Brána** (Trunk Gateway) - zajišťuje propojení s PSTN.

### Úkoly IP telefonie

- **Převod hlasu na IP datagramy**: hlas - **analogový** signál, IP datagram - **digitální** a ještě k tomu nespojitý (nespojitý myšleno, že jsou data přenášena po kusech).
- **Řízení komunikace**: komunikuje se přes ústřednu - gatekeeper (klient-server) a mezi telefony (peer-to-peer). Nejčastější je ale zahájení spojení přes ústřednu a následná peer-to-peer komunikace. Je nutné zajistit:
  - **registraci účastníků** (na ústřednách),
  - **adresování hovorů** pomocí tel. čísel a SIP URI,
  - **směrování hovorů** tj. hledání cesty, kudy budou putovat pakety,
  - **vytváření hovorů** (obvykle peer to peer spojení mezi 2 telefony) a jejich udržování.
- **Připojení** do klasického telefonního systému **PSTN** a **mobilních sítí** pomocí **brány** (trunk gateway).
- **Aplikační služby** jako vyhledávání uživatelů pomocí LDAP nebo WWW či navazování spojení pomocí DNS a DHCP.

### Kódování hlasu

Hlas je nejdříve nutné **navzorkovat** a poté navzorkovaná data **rozdělit do paketů**, což se dělá pomocí **kódování hlasu** (kodeku). Kodeky využívají faktu, že lidská řeč není (obvykle) na celém rozsahu lidského slyšení a **ignorují okrajové frekvence**, tím provádí (ztrátovou) kompresi.

- Lidské **ucho** vnímá na **20 Hz** až **20 kHz**, **řeč** je obvykle na **200 Hz** až **9 kHz** (9 kHz je ale spíš vysoký zpěv).
- U telefonní linky vzorkujeme frekvence **300 H** až **3.4 kHz**, případně až **4 kHz**.
- Pokud chceme vzorkovat **4 kHz** frekvenci, musíme vzorky vytvářet **2x** rychleji (Shannonův teorém) tzn. **8 kHz**. Řekněme, že jeden vzorek má 8 bitů (1 B). Za 1 sekundu budeme muset zpracovat **8000\*8 = 64 kb**. **Šířka pásma** tak bude **64 kb/s**.

Tato šířka pásma bere v potaz pouze samotná data, v paketových sítích je musíme ale zapouzdřit. Na aplikační vrstvě je to protokol **Real-time Transport Protocol** (RTP), který je dále zapojen do **UDP**, **IP** a **Ethernetového rámce**. Data navíc nemůžeme posílat po příliš velkých kusech (problém se ztrátou a zpožděním). Obvykle se posílají data po **20-30 ms**, což může díky hlavičkám jednotlivých protokolů způsobit navýšení potřebné šířky pásma třeba až o polovinu.
![[media/szz-42/media/image9.png]]

### Session Initiation Protocol (SIP)

Aplikační protokol nad UDP určený pro **signalizaci** VoIP (vytáčení atd.), neřeší přenos dat hovoru (k tomu se používá RTP). Zajišťuje:

- **registraci uživatelů** (na bránu),
- **navázání spojení** a **směrování hovorů**,
- **adresování** pomocí SIP URI (**sip:user@domain**) - **adresa** v IP telefonii.

Protokol **neprovádí**: správu relací po jejich vytvoření, nezajišuje kvalitu hovoru, nezajišťuje přenos hlasových dat.

Jedná se o starý protokol a byl navržen na ISO/OSI modelu, používá tak L7 vrstvu.
![[media/szz-42/media/image22.png]]

#### **Architektura SIP**

- **User Agent Server** (UAS - **SIP server**) - může mít jednu nebo více z funkcí:
  - **Proxy server**: analyzuje zprávy a směruje hovory,
  - **Lokalizační server**: má informace o umístění klientů,
  - **Server pro směrování**: není nutný, jedná se pouze jen o další bod spojení. Směrování se provádí buď pomocí DNS nebo staticky (předkonfigurováno). Směrovací informace jsou v **SIP hlavičce**.
  - **Registrační server**: přijímá žádosti REGISTER a aktualizuje lokaci.
- **User Agent Client** (UAC - **SIP klient**) - koncové zařízení, SIP telefon (fyzický nebo SW)

IP telefonie je pomocí SIP **globální** (zahrnuje celý internet) a **distribuovaná** (neexistuje centrální správa, SIP domény se dynamicky propojují). Systém tak umožňuje vyhledat a směrovat hovor na libovolný do sítě zapojený telefon.

#### **Příkazy protokolu SIP**

- **REGISTER** - žádost o registraci,
- **INVITE** - zahájení komunikace vytáčení **volajícím**,
- **OK** - potvrzení komunikace **volaným**,
- **ACK** - potvrzení komunikace **volajícím**, už jde **peer-to-peer**,
- **CANCEL** - zrušení vytváření spojení,
- **BYE** - ukončení vytvořeného spojení, jde **peer-to-peer**,
- **OPTIONS** - získání možností přenosu.

#### **Registrace SIP telefonu**

1. SIP klient pošle svou **IP adresu a port**, na kterém běží IP telefon, SIP serveru ve své doméně.
2. SIP klient mapuje ID uživatele (user SIP URI - sip:user@sip.vutbr.cz) na adresu zařízení (device SIP URI - sip:user@192.168.10.20:5060).
3. Registrační server si udržuje **lokalizační údaje** (SIP URI - IP adresy) o všech svých připojených klientech ve **své SIP doméně**. Používá k tomu **lokalizační databázi**.
![[media/szz-42/media/image6.png]]

#### **Ustanovení hovoru**

1. Volající zašle zprávu **INVITE**, která je směřována architekturou SIP (obecně více proxy serverů) až k příjemci.
2. Volaný (pokud chce komunikovat, tj. zvednutím sluchátka) zasílá zprávu **OK**, která je směřována architekturou SIP zpět k volajícímu.
3. Volající posílá zprávu **ACK** již přímo volanému (peer-to-peer).
4. Probíhá hovor tj. přenos zvukových dat pomocí protokolů **RTP** a **RTCP**.
5. Jeden z účastníků ukončí hovor zprávou **BYE** (peer-to-peer).
6. Druhý odpovídá s **OK**.
![[media/szz-42/media/image18.png]]

### Session Description Protocol (SDP)

Obsahuje **informace** potřebné pro **navázání datového spojení** pro přenos hlasu a videa (použité kodeky, bitrate, IP adresa spojení atd.). Protokol je zapouzdřen do SIP zpráv **INVITE** a **OK** při zahajování přenosu.

### Real-Time Transport Protocol (RTP)

Aplikační protokol pro **přenos hlasových a obrazových dat** pomocí protokolu **UDP**. Pro každý **směr** a typ **médií** se otevírá **samostatný RTP tok**, tzn. při videohovoru má volaný a volající otevřené mezi sebou 4 RTP toky. Hlavička protokolu mimo jiné obsahuje **typ přenášených dat**, **sekvenční číslo** a **časovou značku**, aby bylo možné data poskládat ve správném pořadí, pokud dojde k jejich přehození po cestě.

### RTP Control Protocol (RTCP)

RTCP poskytuje **řídící informace** pro RTP tok dat, ale sám žádná data nenese. Používá se k pravidelnému přenosu **kontrolních** paketů účastníkům streamované multimediální relace. Hlavní funkcí RTCP je **poskytování zpětné** vazby na **kvalitu služeb** (QoS) poskytovanou RTP. Pro zajištění kvality je třeba eliminovat:

- **ozvěnu** (echo),
- **zpoždění paketů**,
- **ztrátu paketů** - ztráta pod 1% znamená dobrou kvalitu, ztráta od 1% do 2.5% je akceptovatelná a ztráta převyšující 5% již má velký dopad na přenos hlasu a videa,
- **rozptyl následujících paketů** (jitter).

### SIP a DNS

- **NAPTR**: DNS záznam, který se nejčastěji používá společně s **IP telefonií**, slouží k mapování adres SIP serverů. Záznamy **NAPTR** se běžně používají pro ověření existence SIP služeb na doméně.

![[media/szz-42/media/image27.png]]

- **SRV**: slouží k vyhledání příslušného SIP serveru.

![[media/szz-42/media/image32.png]]

- **A** nebo **AAAA**: pro vyhledání IP adresy SIP serveru.

### Zabezpečení VoIP

Bezpečnostní **rizika** a jejich řešení:

- **Odposlech**: lze řešit fyzickým zabránění přístupu k síti nebo pomocí zabezpečení spojení (IPSec, Secure RTP)
- **Viry**, **Spam over** **IP Telephony**, **Phishing over IP Telephony**: antivirus, filtry, vzdělání uživatelů.
- **Neautorizované použití**: vyžadovat autentizaci.
- **Výpadky napětí**: Power over Ethernet, záložní zdroje pro IP telefony a síťovou infrastrukturu (switche a routery).

### Alternativní služby k VoIP

- **rozdíly**: Používají proprietární nestandardní protokoly. Mohou používat rozdílnou architekturu (peer-to-peer, hybridní - jako VoIP, pouze klient-server). Proprietární správa účtů. Negarantují službu a nemusí např. poskytovat tísňová volání, což IP telefony musí. Mají omezené možnosti propojení s PSTN, mobilními sítěmi a standardním VoIP.
- **společné vlastnosti**: adresování, směrování a přenos hlasových dat a stím spojené udržování spojení, vytváření účtů a registrace uživatelů a jiné službu kromě hovorů, např. Instant Messaging, přenos souborů, přenos obrazu, sdílení plochy atd.

# Správa sítí

Správa sítí zahrnuje řešení problémů známých pod akronymem **FCAPS**:

- **Fault management**: zaznamenání, izolování a opravení chyby.
- **Configuration management**: zavádění konfigurací zařízení, zálohování konfigurací, zaznamenávání změn, aktualizace SW.
- **Accounting management**: zisk statistik využitívání sítě (např. IP telefonie) a s tím spojené účtování.
- **Performance management**: zajištění dostatečného výkonu sítě (např. šířky pásma pro VoIP).
- **Security management**: zabezpečení sítě (autentizace, autorizace, zabránění fyzického přístupu k zařízením atd.).

## Simple Network Management Protocol (SNMP)

SNMP je protokol pro přenos informací o zařízeních na síti, pod pojmem SNMP ale obecně myslíme celý mechanismus aktivní správy sítí (dalšími aktivními jsou např. ICMP ping, telnet, PortQuery, …) za použití tohoto protokolu. SNMP zpráva sítě je tvořena:

- **Management Station**: jedná se o server na kterém běží SW, který se pomocí **protokolu SNMP** obvykle pravidelně dotazuje (polling) **SNMP agentů** na portu **161** a stahuje si od nich tak **monitorovací informace**, které ukládá a např. umožňuje nějak graficky zobrazit. Dotazy na data **MS** realizuje příkazy **Get**, **GetNext**, **GetBulk** a MS také může konfigurovat SNMP agenta pomocí příkazu **Set**.
- **SNMP Agent**: jedná se o **zařízení v síti** (switche, routery, tiskárny, počítače atd.), u síťových zařízení je nainstalován SW pro SNMP protokol obvykle od výrobců, na PC si jej musíme stáhnout. SNMP agent **sbírá informace o zařízení**, na kterém běží (např. vytížení CPU, vytížení paměti, stav toneru, počet papírů v zásobníku, počet odeslaných paketů, počet přijatých paketů atd.) a na vyzvání Management Station je jí odesílá. Nevede si však historii, tu musí zaznamenávat MS. SNMP agent může kontaktovat MS **sám** od sebe při **vzniku** nějaké závažné **chyby** (nakonfigurováno jaká chyba, resp. jaká úroveň závažnosti). Tato komunikace je realizována pomocí **asynchronní** (tj. MS si ji nevyžádala) zprávy **Trap** na portu **162**.
- **SNMP protokol**: **nestavový** protokol sloužící pro přenos informací o zařízeních na síti, jedná se o protokol typu request-response a existuje několik verzí **SNMP**, **SNMPv2** (přidává autentizaci), **SNMPv3** (přidává šifrování).
![[media/szz-42/media/image30.png]]

![[media/szz-42/media/image2.png]]

### Monitorované objekty

Objekty jsou uspořádané do **skupin** v **databázi objektů MIB** (Management Information Base). Databáze MIB má stromovou strukturu:

- **nelistové uzly**: reprezentují skupiny objektů,
- **listové uzly**: reprezentují konkrétní objekt.

Objekty jsou adresováný pomocí **OID**, které **reprezentuje cestu ve stromové struktuře** a má tvar čísel oddělených tečkami, kde čísla identifikují uzel na dané úrovni stromu a tvoří tak cestu. Např. **OID 1.3.6.1.2.1.4** představuje objekt **ip**.
![[media/szz-42/media/image3.png]]

#### **Definice monitorovaných objektů**

Objekty jsou definovány a popisovány pomocí jazyka **Structure Management Information** (SMI). Popis objektu je tvořen:

- **jménem objektu,** což je **OID** - jednoznačný identifikátor objektu,
- **syntaxí**, která určuje (abstraktní) datový typ spojený s objektem, např (**Counter32** - přeteče zpět na 0, **Gauge32** - nepřeteče a setrvává na max hodnotě, **OBJECT IDENTIFIER**, **SEQUENCE**, **INTEGER**, **IpAddress, NetworkAddress**, **OCTET STRING**, …)
- **kódováním pro přenos po síti** - používá se kování **BER**.

Příklad definice objektu **ipInDelivery** ve **skupině ip**:
![[media/szz-42/media/image15.png]]

### Basic Encoding Rules (BER)

Jedná se o binární kódování informací po za sebou jdoucích trojicích tvořených:

- **Type**: typ objektu uložen v **1. bytu**.
- **Length**: délka hodnoty v bytech, implicitně je uložena pouze na 1 B (tj. na druhém bytu). Pokud nelze vyjádřit na 1 B (tj. v tomhle případě větší než 0x80), pak je délka vyjádřena v **N** následujících bytech a **N = hodnota druhého B - 0x80**.
  - Když se ti nevleze délka do 2. bytu, specifikuješ v něm, na kolika následujících bytech je uložena délka. Tj., pokud má být délka na 4 bytech, bude ve 2. bytu hodnota 0x84 a délka dat bude specifikovaná od 3. do 7. bytu, data samotná pak budou začínat na 8 bytu a budou mít délku specifikovanou na těch 4 bytech.
- **Value**: hodnota záznamu.
![[media/szz-42/media/image26.png]]

### Nasazení SNMP

Při praktickém nasazení SNMP musíme brát v potaz:

- **kolik zařízení** bude monitorováno,
- jaká bude **frekvence sběru** dat,
- jaký bude **objem přenášených dat**.

Tyto tři faktory musí být vyváženy tak, aby nepředstavovaly významné zatížení sítě. Dále musíme brát v potaz, že protokol **SNMP** je **zapouzdřen do UDP** a může tak docházet ke **ztrátám** datagramů (není zde potvrzení). Např. zpráva **Trap nemusí dorazit** nebo zápis konfigurace pomocí příkazu **Set se nemusí provést** atd. Systém SNMP je **centralizovaný** a všechna data jsou na jedné stanici (Management Station), při poruše této stanice ztrácíme přehled o síti. Měli bychom používat **šifrovanou verzi** SNMPv3 kvůli **bezpečnosti**, pokud by se někdo naboural do sítě a zde běželo SNMP starších verzí, získá informace o téměř všech zařízeních. Program pro SNMP: **snmpwalk**.

## NetFlow

NetFlow narozdíl od SNMP neumožňuje monitorovat zařízení v síti a získávat informace jako zatížení CPU a paměti, stav toneru, počet papírů v tiskárně atd. NetFlow se zaměřuje více na monitorování komunikace na síti v podobě síťových toků, tj.:

- **kdo a s kým komunikuje** (IP adresy a jiné adresy),
- **kolik dat si posílají**,
- **kdy komunikují**,
- **jaké používají protokoly**,
- atd.

Informace o stavu zařízení a jestli funguje nelze získat pomocí NetFlow. NetFlow byl původně **proprietární** protokol vyvinutý firmou **Cisco**, dnes je již **standardizován** pomocí **RFC**. Stejně jako u SNMP nepovažujeme NetFlow pouze za protokol, ale mechanismus monitorování a správy sítě. Architektura NetFlow je tak tvořena:

- **Exportérem**: jedná se o sondu/router pro získávání statistik o tocích. Často se jedná o samostatnou sondu která pouze **odposlouchává** provoz a zaznává jej, protože řešení v rámci routeru může být příliš drahé.
- **Kolektorem**: zařízení, které ukládá záznamy o tocích. Jedná se o nějaký server (podobně jako MS u SNMP), tzn. **centralizované** řešení.
- **Protokolem**: NetFlow_v5, NetFlow_v9, IPFIX.
- **Nástroje pro zobrazení dat**: grafy, statistiky, výpisy atd.

### Síťový tok

**Posloupnost paketů** mající **společnou vlastnost** (např. IP adresu), které prochází určitým **bodem pozorování** za **určitý časový** interval. Záznam o toku obsahuje informace o toku, **nikoliv přenášená data**. Mezi tyto informace patří:

- zdrojová a cílová **IP adresa**,
- zdrojový a cílový **port**,
- **typ protokolu** (může být z více vrstev tj. transportní a aplikační),
- **časové razítko** (obsahuje začátek a konec toku),
- **počet přenesených dat** v B.
![[media/szz-42/media/image4.png]]

### Exportér NetFlow

**Síťové zařízení** a software (často dedikované - sonda), které **monitoruje** procházející provoz. Výtváří **záznamy** o tocích a **aktualizuje** starší záznamy ve své **NetFlow cache**. **Vyhledávání** záznamů pro aktualizaci provádí **pomocí heše** informací identifikující tok (IP adresy a porty). To znamená, že pro **každou komunikaci vytváří 2 toky** (záleží na směru). Exportér také může provádět nějaké agregace dat, více viz dále. Na rozdíl od SNMP odesílají **exportéry** data kolektoru **sami bez vyžádání** po:

- **ukončení toku** (TCP - **FIN**, **RST**),
- po **vypršení časovače**
  - **neaktivní timeout**: nebyl odeslán žádný paket v daném toku (defaultně 15 s),
  - **aktivní timeout**: odesílá data u příliš dlouhých nepřerušovaných toků, může jít např. o nějaké stahování (délka může být třeba 30 min),
- **zaplnění** NetFlow **cache**.

### Kolektor NetFlow

Kolektor je na síti **jeden** a přijímá pakety NetFlow z **jednoho či více exportérů**. Jeho funkce jsou poté následující:

- **Zpracování záznamů** o tocích a jejich **ukládání** na disk nebo do databáze, ukládají se binárně ve formátu optimalizovaném pro vyhledávání (před uložením mohou být data **agregována**),
- **Grafické zobrazování** dat (např. nějaká **heat mapa** vytíženosti) pomocí SW, např. **Flowmon**,
- **Realizovat dotazování** nad daty pomocí např. **nfdump** (provádět agregace uložených neagregovaných dat - chci zobrazit všechny toky z jedné IP, druhá mě ale nezajímá, a sečíst objem přenesených dat - typický příklad pro účtování),
- **Automatizace** např. automatické odhalení anomálií - podezřelých toků (PC v kanceláři s pracovní dobou od 9 do 17 začne ve 22 posílat/přijímat velké množství dat → možná je to útok).

### Protokol NetFlow
![[media/szz-42/media/image12.png]]

Příklad paketu **verze 5**:

Paket je tvořen:

- **hlavičkou**, která obsahuje
  - počet NetFlow záznamů přenášených v datové části,
  - čas odeslání tohoto NetFlow paketu,
  - identifikaci sondy, ze které byl paket odeslán
  - atd.
- **daty** (obsah paketu) obsahuje množinu záznamů o tocích, každý záznam představuje statistiku o jednom toku.

#### **Vylepšení ve verzi 9 a IPFIX (IP Flow Information Export)**

NetFlow verze **5** má **fixní** formát (neumožňuje např. export IPv6 adres), **verze 9** to řeší zavedením **šablon**. Hlavička zůstává a obsahuje informaci o **ID šablony**, podle které jsou zapsána data v datové části paketu (šablony zasílá exportér kolektoru, ten si ji pak zapamatuje a již není součástí paketů - datová část tak může obsahovat šablony, informace o datových tocích nebo oboje, **většinou** ale **pouze** informace o **datových tocích**). **IPFIX** je poté ještě **více flexibilní**, definuje více polí, které lze použít v šablonách, jinak se výrazně neliší.

### Použití NetFlow

- **Monitorování sítě**, plánování sítě, **bezpečnostní analýza**,
- Sledování aplikací, uživatelů a zajištění **účtování**,
- **Dlouhodobé ukládání** informací o tocích (někteří poskytovatelé to mají dané ze zákona - pak je nutné počítat poměrně s velkou paměťovou náročností objem NetFlow statistik je roven asi 1-2 % objemu provozu sítě, tj. při denní zátěži 100 GB bude třeba uložit 1-2 GB NetFlow dat denně po dobu jednoho roku: (1 až 2) \* 365 GB).

## Zdroje

- SZZ okruh 42 — studijní materiály FIT BUT (`szz-42.docx`). Obrázky: `media/szz-42/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[topics/41-assembler|41. Programování v JSI (assembler)]] · další: [[topics/43-tcp-ip-komunikace|43. TCP/IP komunikace]] ▶
