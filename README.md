# naBalety
Project for event organization firm naBalety

Celem jest stworzenie serwisu do tworzenia i zarządzania wydarzeń
W jego skład wchodzą:
- System paginacji frameworku Django - faza testów
- Serwis zarządzający tworzeniem wydarzeń - zrobiony
- System sprzedaży biletów - do implementacji
- Mechanizmy kontrolujące obecne pule - faza testów
- System autoryzacji użytkownika - do implementacji
- Galeria zdjęć dla użytkownika - w późniejszym terminie
- System kasowania biletu przez kod QR - do implementacji
- System płatności - do implementacji
- Panel użytkownika z counterem do 10 w celu darmowych wejść - do implementacji

Obsługa dodawania ewentu:
Dodając event musimy mieć wcześniej określoną ilość pul łącznie z ilością biletów w konkretnych pulach, 
jeśli wydarzenie ma mieć 3 pule należy pamiętać żeby nie ustawiać daty zakończenia trzeciej puli,
rozpoczęcie wydarzenia jest automatycznie wybierane jako zakońćzenie ostatniej puli

Na chwilę obecną diagram klas wygląda tak, bardzo możliwe że pojawią się nowe pola w ramach tego jaki potrzeby pojawią się podczas rozwoju serwisu
![uml-graph](https://user-images.githubusercontent.com/73855075/155544438-9fac13bb-ced7-422c-9657-5074f91be810.png)


**./website/models.py**
W tym pliku określam modele które następnie zostają wyeksportowane do bazy danych (obecnie znajduje się lokalnie) 

**./website/admin.py**
Służy do rejestrowania modeli w panelu administratora, pozwala to na późniejszy wgląd i edycję bazy danych z poziomu panelu

**./website/urls.py**
Łączy określony url z widokiem

**./website/views.py**
Służy do połączenia widoku z odpowiednim templatem, w tym miejscu wykonuje się też logika widoków, szczególną metodą wartą uwagi jest system wyświetlania puli
![image](https://user-images.githubusercontent.com/73855075/155545519-39cb3d55-e4c7-4260-a4f2-d55d48d05471.png)
