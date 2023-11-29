Projekti i dyte ne lenden Rrjeta Kompjuterike qe paraqet aplikimin e sockets dhe protokollit UDP per komunikim ne gjuhen Python!

Programi eshte i organizuar ne dy skripta server.py dhe client.py, per ekzekutim duhet te behet run se pari server.py

SERVERI:
1. Të vendosen variabla te cilat përmbajnë numrin e portit (numri i portit të jetë i
çfarëdoshëm) dhe IP adresën;
2. Të jetë në gjendje të dëgjojë (listën) të paktën të gjithë anëtaret e grupit;
3. Të pranojë kërkesat e pajisjeve që dërgojnë request (ku secili anëtar i grupit duhet ta
ekzekutojë të paktën një kërkesë në server);
4. Të jetë në gjendje të lexoje mesazhet që dërgohen nga klientët;
5. Të jetë në gjendje të jap qasje të plotë të paktën njërit klient për qasje në folderat/
përmbajtjen në file-t në server.

KLIENTI:
1. Të krijohet socket lidhja me server;
2. Njeri nga pajisjet (klientët) të ketë privilegjet write(), read(), execute();
3. Klientët tjerë të kenë vetëm read() permission;
4. Të behet lidhja me serverin duke përcaktuar saktë portin dhe IP Adresën e serverit;
5. Të definohen saktë socket-at e serverit dhe lidhja të mos dështojë;
6. Të jetë në gjendje të lexojë përgjigjet që i kthehen nga serveri;
7. Të dërgojë mesazh serverit si në formë të tekstit;
8. Të ketë qasje të plotë në folderat/përmbajtjen në server.

   
