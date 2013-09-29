package main

import "fmt"
import "net"

func echoing(c net.Conn, l *net.TCPListener) {
  b := make([]byte,100,100)
  for true {
    n, _ := c.Read(b)
    b = b[0:n]
    c.Write(b)
  }
}

func main() {
  //b := make([]byte,100,100)
  var laddr *net.TCPAddr
  addr := net.JoinHostPort("192.168.0.100","31337")
  laddr, _ = net.ResolveTCPAddr("tcp",addr)
  l,_ := net.ListenTCP("tcp",laddr)
  var c net.Conn
  for {
    c, _ = l.Accept()
    go echoing(c,l)
  }
  var d uint32
  fmt.Scanf("%d",&d)
}
