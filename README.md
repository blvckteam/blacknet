# BlackNet - Полноценная onion-поисковая-система в твоем терминале!
<p align="center">
  <img src="https://github.com/blvckteam/blacknet/blob/main/imgs/logo.png?raw=true">
</p>

## О BlackNet
BlackNet это простая утилита написаная на Python 3.9, которая позволяет искать сайты .onion по ключевым словам. BlackNet использует darksearch.io API, все права защищены.
## Установка
1) ``git clone https://github.com/blvckteam/blacknet``<br/>
2) ``cd darkdump``<br/>
3) ``python3 -m pip install -r requirements.txt``<br/>
4) ``python3 main.py --help``<br/>
## Использование 
Пример 1: ``python3 main.py --query programming``<br/>
Пример 2: ``python3 main.py --query="chat rooms"``<br/>
Пример 3: ``python3 main.py --query hackers --page 2``<br/>
 - Примечаниe: Аргумент --page отображает определенное кол-во страниц с результата поиска.<br/>
## Меню
```

    ____  __    ___   ________ __ _   ______________
   / __ )/ /   /   | / ____/ //_// | / / ____/_  __/
  / __  / /   / /| |/ /   / ,<  /  |/ / __/   / /   
 / /_/ / /___/ ___ / /___/ /| |/ /|  / /___  / /    
/_____/_____/_/  |_\____/_/ |_/_/ |_/_____/ /_/     
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

usage: darkdump.py [-h] [-v] -q QUERY [-p PAGE]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         returns darkdump's version
  -q QUERY, --query QUERY
                        the keyword or string you want to search on the deepweb
  -p PAGE, --page PAGE  the page number to filter through the results that the search engine returns (default=1).

```
## Визуальная часть
<p align="center">
  <img src="https://github.com/blvckteam/blacknet/blob/main/imgs/blacknet_ex.png?raw=true">
</p>

## Внимание
Данный репозиторий является не оффициальным форком на [darkdump](https://github.com/josh0xA/darkdump). Автор не несет ответственности за точность, полноту или качество предоставленной информации. Никакие претензии за материальный или нематериальный ущерб, вызванный использованием или неиспользованием предоставленной информации либо использованием неверной или неполной информации, не принимаются, если этот ущерб не был явным следствием небрежности или преступного умысла автора. Все предложения выдвигаются без каких-либо обязательств. Автор оставляет за собой право изменять, удалять или дополнять содержимое веб-сайта без предварительного уведомления, а также удалять публикации в Интернете временно или навсегда.
