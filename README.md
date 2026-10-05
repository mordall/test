mapa.py wersja 0.11
Generowanie mapy ze śladami wycieczek pieszych (lub jakichkolwiek innych).
Stworzone z pomocą Claude
Konieczny zainstalowany najnowszy python

Najpierw tworzymy mapę ze śladami (gdy dojdzie kilka nowych - tworzymy nową mapę)

eksloator plikow/wchodzimy do katalogu gdzie znajdują się slady GPS i mapa.py, w pasku wpisujemy cmd i wpisujemy 

python mapa.py

mapa zostanie wygenerowana

przegladanie mapy

Na komputerze
wlaczamy serwer python -m http.server 8000
wchodzimy przez przeglądarke na adres: http://localhost:8000/moje_trasy.html
gdy skonczymy zamykamy serwer: bedac w terminalu - ctrl+c i enter. upewnic sie ze strona przestala dzialac.

mapa może być też umieszczona w internecie np na github 
przykład: https://mordall.github.io/test/moje_trasy.html
umieszczamy plik moje_trasy.html na serwerze
