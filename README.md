**English below..**

See on **Failisüsteemi hägutestimise raamistik**, mis on minu arvutiteaduse bakalaureusetöö teemaks.

Juhendajad: **Meelis Roos** ja **Kristjan Krips**. 

Raamistik on arendatud User-mode Linuxi peal, mis kasutas kernelit versiooniga 4.11. http://user-mode-linux.sourceforge.net

**Failide selgitus:**

Töö aluseks oli võetud Linuxi kernel aadressilt https://github.com/torvalds/linux.

* Kaustast _arch/um/_ on UML-i ja kliendipoolsed failid

    _drivers/ubd_kern.c_ ketta lugemise vahelevõtmine
    
    _include/shared/os.h_ lisafunktsiooni defineerimine
    
    _os-Linux/file.c_ kliendi lisafunktsioon

* kaustast _server/_ serveri pool

    _server.py_
    
* _.config_ fail on UML-i seadistus, seda ei tohiks muuta


**Raamistiku paigutus ja seadistamine:**

Esiteks läheb vaja Linuxit. Arenduses kasutati Linux Mint 18 “Sarah” – Cinnamon (64-bit), mis on vabavarana kättesaadav [siin](https://linuxmint.com/edition.php?id=217). Läheb tarvis Pythonit versiooniga 3.5. Samuti läheb tarvis programmi Screen, Linux Mint peale saab seda installida käskudega:

`sudo apt-get update `

`sudo apt-get install screen`

1. Tuleb laadida alla ja pakida lahti kernel, arenduses kasutati versiooni **4.11.** https://www.kernel.org/
2. Asendada lahtipakitud failid nendega, mis on selle repositooriumis.
3. Tuleb implementeerida vajalikud hägurid, peale seda saab neid kasutada failis [...]/server/server.py
4. Käivitada raamistiku serveri pool, kaustas /server käsuga `python3.5 server.py`
5. Tekitatakse ketta pilt ning vormindatakse seda vajaliku Linuxi failisüsteemiga
6. Kompileerida UML käsuga `make ARCH=um` ning käivitada see käsuga (tekitatud ketta pilt asendada "[virtuaalketa 2 asukoht]" asemele)

`./linux mem=256M ubd0=[virtuaalketta 1 asukoht] root=/dev/ubda umid=testmasin ubd1=[virtuaalketa 2 asukoht]`

7. Uues konsoolis sisestada käsk `screen /dev/pts/Y` ,kus "/dev/pts/Y" on UML-i õnnestunud käivitamise järgselt konsooli ilmunud teated kujul "Virtual console X assigned device '/dev/pts/Y'"
8. Kasutaja == parool == root
9. Korrektseks UML-i peatamiseks on olemas käsk `halt`

***

**English here**

This is a **File fuzz testing framework**, which is my BCompSc thesis.

Supervised by **Meelis Roos** and **Kristjan Krips**.


The framework was developed on User-mode Linux on kernel v4.11. http://user-mode-linux.sourceforge.net

**File explanation:**

The basis for this thesis was taken from https://github.com/torvalds/linux.

* Kaustast _arch/um/_ UML and client side

    _drivers/ubd_kern.c_ intercept image reading
    
    _include/shared/os.h_ define function
    
    _os-Linux/file.c_ client side

* kaustast _server/_ server side

    _server.py_
    
* _.config_ UML settings file, should not be edited
    

**Installing the framework:**

First you need Linux. During the development a Linux Mint 18 “Sarah” – Cinnamon (64-bit) was used which can be downloaded [here](https://linuxmint.com/edition.php?id=217). You will need Python3.5. Also Screen which can be install with 

`sudo apt-get update`

`sudo apt-get install screen`

1. You will need to download and unzip kernel, development was done on version **4.11.** https://www.kernel.org/
2. Replace unzip files with the ones in this repo.
3. Fuzzers will need to be implemented after that they can be used in [...]/server/server.py
4. Start frameworks server part `python3.5 server.py`
5. Create disc image with needed filesystem
6. Compile UML with `make ARCH=um` and start it with put created disc image instead of "[dirtual disc 2 path]")

`./linux mem=256M ubd0=[virtuaalketta 1 asukoht] root=/dev/ubda umid=testmasin ubd1=[dirtual disc 2 path]`

7. Open new console and enter `screen /dev/pts/Y` where "/dev/pts/Y" is a message that appears after a successful UML initiation and the messages should look like this: "Virtual console X assigned device '/dev/pts/Y'"
8. User == password == root
9. A polite way to stop UML is with a `halt` command
