var lp_token = "PGRpdiBjbGFzcz0iaXotcm93IGl6LXJvdy0tZmxleC1lbmQgbGFyYXB1c2gtb3B0aW4tLWJyYW5kaW5nLXdyYXBwZXIgbGFyYXB1c2gtb3B0aW4tLWJyYW5kaW5nLXdyYXBwZXItZGlhbG9nLWJveCBpemJyYW5kaW5nIj4KICA8YSBocmVmPSJodHRwczovL2xhcmFwdXNoLmNvbS8/dXRtX21lZGl1bT1wdXNoJnV0bV9zb3VyY2U9eXRzaG9ydHMuc2F2ZXR1YmUubWUmdXRtX3JlZj0iIHRhcmdldD0iX2JsYW5rIiBjbGFzcz0ibGFyYXB1c2gtb3B0aW4tLWJyYW5kaW5nLXRleHQgbGFyYXB1c2gtb3B0aW4tLWJyYW5kaW5nLXRleHQtZGlhbG9nLWJveCI+CiAgICBQb3dlcmVkIGJ5IDxzcGFuIGNsYXNzPSJsYXJhcHVzaC1vcHRpbi0tbGFyYXB1c2gtdHh0Ij5MYXJhUHVzaDwvc3Bhbj48L2E+CjwvZGl2Pg=="
var lp_base = 'PGRpdiBpZD0ibGFyYXB1c2gtb3B0aW4iIGNsYXNzPSJsYXJhcHVzaC1vcHRpbi0tZGlhbG9nLWJveCBsYXJhcHVzaC1vcHRpbi0tcHJldmlldy1jb250YWluZXIiPjxkaXYgY2xhc3M9Iml6LXJvdyBpei1yb3ctLXNwYWNlLWJ0d24iPjxkaXYgY2xhc3M9Iml6LWNvbCBpei1jb2wtLWNvbnRlbnQtY2VudGVyIGxhcmFwdXNoLW9wdGluLS1pY29uLXdyYXBwZXIgbGFyYXB1c2gtb3B0aW4tLW1yLTEwIj4gPGltZyB3aWR0aD0iNDAiIGFsdD0iRGVmYXVsdCBPcHQtaW4gSWNvbiIgY2xhc3M9ImxhcmFwdXNoLW9wdGluLS1pY29uIj48L2Rpdj48ZGl2IGNsYXNzPSJsYXJhcHVzaC1vcHRpbi0tY29udGVudCI+PGRpdiBjbGFzcz0ibGFyYXB1c2gtb3B0aW4tLXRpdGxlIj4gPHNwYW4gY2xhc3M9ImxhcmFwdXNoLW9wdGluLS1saW5lLWNsYW1wIGxhcmFwdXNoLW9wdGluLS1saW5lLWNsYW1wLTIgbGFyYXB1c2gtb3B0aW4taGVhZGluZyI+PC9zcGFuPjwvZGl2PjxkaXYgY2xhc3M9ImxhcmFwdXNoLW9wdGluLS1tZXNzYWdlIGxhcmFwdXNoLW9wdGluLS1tdC01Ij4gPHNwYW4gY2xhc3M9ImxhcmFwdXNoLW9wdGluLS1saW5lLWNsYW1wIGxhcmFwdXNoLW9wdGluLS1saW5lLWNsYW1wLTIgbGFyYXB1c2gtb3B0aW4tc3ViaGVhZGluZyI+PC9zcGFuPjwvZGl2PjwvZGl2PjwvZGl2PiA8ZGl2IGNsYXNzPSJpei1yb3cgaXotcm93LS1mbGV4LWVuZCBsYXJhcHVzaC1vcHRpbi0tY3Rhcy1jb250YWluZXIgbGFyYXB1c2gtb3B0aW4tLW10LTE1IGxhcmFwdXNoLW9wdGluLS1tYi01Ij4gPGJ1dHRvbiBjbGFzcz0ibGFyYXB1c2gtb3B0aW4tLWN0YSBsYXJhcHVzaC1vcHRpbi0tY3RhLWxhdGVyIGxhcmFwdXNoLW9wdGluLS1tci0xMCI+PC9idXR0b24+IDxidXR0b24gY2xhc3M9ImxhcmFwdXNoLW9wdGluLS1jdGEgbGFyYXB1c2gtb3B0aW4tLWN0YS1hbGxvdyI+PC9idXR0b24+PC9kaXY+PC9kaXY+'
var lp_cs= 'I2xhcmFwdXNoe2Rpc3BsYXk6YmxvY2shaW1wb3J0YW50fSNsYXJhcHVzaC1vcHRpbntkaXNwbGF5Om5vbmV9I2xhcmFwdXNoLW9wdGluIC5sYXJhcHVzaC1vcHRpbi0tbXItNXttYXJnaW4tcmlnaHQ6NXB4fSNsYXJhcHVzaC1vcHRpbiAubGFyYXB1c2gtb3B0aW4tLW1yLTEwe21hcmdpbi1yaWdodDoxMHB4fSNsYXJhcHVzaC1vcHRpbiAubGFyYXB1c2gtb3B0aW4tLW1yLTE1e21hcmdpbi1yaWdodDoxNXB4fSNsYXJhcHVzaC1vcHRpbiAubGFyYXB1c2gtb3B0aW4tLW1yLTIwe21hcmdpbi1yaWdodDoyMHB4fSNsYXJhcHVzaC1vcHRpbiAubGFyYXB1c2gtb3B0aW4tLW10LTV7bWFyZ2luLXRvcDo1cHh9I2xhcmFwdXNoLW9wdGluIC5sYXJhcHVzaC1vcHRpbi0tbXQtMTB7bWFyZ2luLXRvcDoxMHB4fSNsYXJhcHVzaC1vcHRpbiAubGFyYXB1c2gtb3B0aW4tLW10LTE1e21hcmdpbi10b3A6MTVweH0jbGFyYXB1c2gtb3B0aW4gLmxhcmFwdXNoLW9wdGluLS1tdC0yMHttYXJnaW4tdG9wOjIwcHh9I2xhcmFwdXNoLW9wdGluIC5sYXJhcHVzaC1vcHRpbi0tbWItNXttYXJnaW4tYm90dG9tOjVweH0jbGFyYXB1c2gtb3B0aW4gLmxhcmFwdXNoLW9wdGluLS1tYi0xMHttYXJnaW4tYm90dG9tOjEwcHh9I2xhcmFwdXNoLW9wdGluIC5sYXJhcHVzaC1vcHRpbi0tbWItMTV7bWFyZ2luLWJvdHRvbToxNXB4fSNsYXJhcHVzaC1vcHRpbiAubGFyYXB1c2gtb3B0aW4tLW1iLTIwe21hcmdpbi1ib3R0b206MjBweH0jbGFyYXB1c2gtb3B0aW4gLmxhcmFwdXNoLW9wdGluLS1tbC01e21hcmdpbi1sZWZ0OjVweH0jbGFyYXB1c2gtb3B0aW4gLmxhcmFwdXNoLW9wdGluLS1tbC0xMHttYXJnaW4tbGVmdDoxMHB4fSNsYXJhcHVzaC1vcHRpbiAubGFyYXB1c2gtb3B0aW4tLW1sLTE1e21hcmdpbi1sZWZ0OjE1cHh9I2xhcmFwdXNoLW9wdGluIC5sYXJhcHVzaC1vcHRpbi0tbWwtMjB7bWFyZ2luLWxlZnQ6MjBweH0jbGFyYXB1c2gtb3B0aW4gLmxhcmFwdXNoLW9wdGluLS1saW5lLWNsYW1we2Rpc3BsYXk6YmxvY2s7ZGlzcGxheTotd2Via2l0LWJveDstd2Via2l0LWJveC1vcmllbnQ6dmVydGljYWw7cG9zaXRpb246cmVsYXRpdmU7bGluZS1oZWlnaHQ6MS4yNTt3b3JkLWJyZWFrOmJyZWFrLXdvcmQ7b3ZlcmZsb3c6aGlkZGVuO3RleHQtb3ZlcmZsb3c6ZWxsaXBzaXM7cGFkZGluZzowfSNsYXJhcHVzaC1vcHRpbiAubGFyYXB1c2gtb3B0aW4tLWxpbmUtY2xhbXAtMiwjbGFyYXB1c2gtb3B0aW4gLmxhcmFwdXNoLW9wdGluLS1saW5lLWNsYW1wLTR7bGluZS1oZWlnaHQ6MS4yNWVtIWltcG9ydGFudH1Ac3VwcG9ydHMgKC13ZWJraXQtbGluZS1jbGFtcDoxKXsjbGFyYXB1c2gtb3B0aW4gLmxhcmFwdXNoLW9wdGluLS1saW5lLWNsYW1wOmFmdGVye2Rpc3BsYXk6bm9uZSFpbXBvcnRhbnR9fSNsYXJhcHVzaC1vcHRpbiAubGFyYXB1c2gtb3B0aW4tLWxpbmUtY2xhbXAtMXstd2Via2l0LWxpbmUtY2xhbXA6MTttYXgtaGVpZ2h0OmNhbGMoMWVtICogMS41ICogMSl9I2xhcmFwdXNoLW9wdGluIC5sYXJhcHVzaC1vcHRpbi0tbGluZS1jbGFtcC0yey13ZWJraXQtbGluZS1jbGFtcDoyO21heC1oZWlnaHQ6Y2FsYygxZW0gKiAxLjUgKiAyKX0jbGFyYXB1c2gtb3B0aW4gLmxhcmFwdXNoLW9wdGluLS1saW5lLWNsYW1wLTN7LXdlYmtpdC1saW5lLWNsYW1wOjM7bWF4LWhlaWdodDpjYWxjKDFlbSAqIDEuNSAqIDMpfSNsYXJhcHVzaC1vcHRpbiAubGFyYXB1c2gtb3B0aW4tLWxpbmUtY2xhbXAtNHstd2Via2l0LWxpbmUtY2xhbXA6NDttYXgtaGVpZ2h0OmNhbGMoMWVtICogMS41ICogNCl9I2xhcmFwdXNoLW9wdGluIC5sYXJhcHVzaC1vcHRpbi0tbGluZS1jbGFtcC01ey13ZWJraXQtbGluZS1jbGFtcDo1O21heC1oZWlnaHQ6Y2FsYygxZW0gKiAxLjUgKiA1KX0jbGFyYXB1c2gtb3B0aW4gLmxhcmFwdXNoLW9wdGluLS1saW5lLWNsYW1wLTh7LXdlYmtpdC1saW5lLWNsYW1wOjg7bWF4LWhlaWdodDpjYWxjKDFlbSAqIDEuNSAqIDgpfSNsYXJhcHVzaC1vcHRpbiAuaXotcm93e2Rpc3BsYXk6ZmxleH0jbGFyYXB1c2gtb3B0aW4gLml6LXJvdy0tc3BhY2UtYnR3bntqdXN0aWZ5LWNvbnRlbnQ6c3BhY2UtYmV0d2Vlbn0jbGFyYXB1c2gtb3B0aW4gLml6LXJvdy0tZmxleC1lbmR7anVzdGlmeS1jb250ZW50OmZsZXgtZW5kfSNsYXJhcHVzaC1vcHRpbiAuaXotY29se2Rpc3BsYXk6ZmxleDtmbGV4LWRpcmVjdGlvbjpjb2x1bW59I2xhcmFwdXNoLW9wdGluIC5pei1jb2wtLWNvbnRlbnQtY2VudGVye2p1c3RpZnktY29udGVudDpjZW50ZXJ9QC13ZWJraXQta2V5ZnJhbWVzIGxhcmFwdXNoU2xpZGVJbkRvd257MCV7LXdlYmtpdC10cmFuc2Zvcm06dHJhbnNsYXRlM2QoLTUwJSwtMTAwJSwwKTt0cmFuc2Zvcm06dHJhbnNsYXRlM2QoLTUwJSwtMTAwJSwwKTt2aXNpYmlsaXR5OnZpc2libGV9dG97LXdlYmtpdC10cmFuc2Zvcm06dHJhbnNsYXRlM2QoLTUwJSwwLDApO3RyYW5zZm9ybTp0cmFuc2xhdGUzZCgtNTAlLDAsMCl9fUBrZXlmcmFtZXMgbGFyYXB1c2hTbGlkZUluRG93bnswJXstd2Via2l0LXRyYW5zZm9ybTp0cmFuc2xhdGUzZCgtNTAlLC0xMDAlLDApO3RyYW5zZm9ybTp0cmFuc2xhdGUzZCgtNTAlLC0xMDAlLDApO3Zpc2liaWxpdHk6dmlzaWJsZX10b3std2Via2l0LXRyYW5zZm9ybTp0cmFuc2xhdGUzZCgtNTAlLDAsMCk7dHJhbnNmb3JtOnRyYW5zbGF0ZTNkKC01MCUsMCwwKX19I2xhcmFwdXNoLW9wdGluLmxhcmFwdXNoLW9wdGluLS1wcmV2aWV3LWNvbnRhaW5lcntwb3NpdGlvbjpmaXhlZDt6LWluZGV4Ojk5OTk5OTk5O2JveC1zaXppbmc6Ym9yZGVyLWJveDtjb2xvcjpyZ2JhKDAsMCwwLC44Nyk7Zm9udC1mYW1pbHk6QXJpYWwsIkhlbHZldGljYSBOZXVlIixzYW5zLXNlcmlmIWltcG9ydGFudH0jbGFyYXB1c2gtb3B0aW4ubGFyYXB1c2gtb3B0aW4tLWRpYWxvZy1ib3h7d2lkdGg6NDAwcHg7dG9wOjA7Ym90dG9tOnVuc2V0O2xlZnQ6NTAlO2JhY2tncm91bmQ6I2ZmZjt0cmFuc2Zvcm06dHJhbnNsYXRlKC01MCUsMCk7Ym9yZGVyLXJhZGl1czowIDAgMnB4IDJweDtib3gtc2hhZG93OjAgLTJweCAxNnB4IHJnYmEoMCwwLDAsLjEpO3BhZGRpbmc6MTZweCAxM3B4O3dlYmtpdC1hbmltYXRpb24tbmFtZTpsYXJhcHVzaFNsaWRlSW5Eb3duO2FuaW1hdGlvbi1uYW1lOmxhcmFwdXNoU2xpZGVJbkRvd247d2Via2l0LWFuaW1hdGlvbi1kdXJhdGlvbjouOHM7YW5pbWF0aW9uLWR1cmF0aW9uOi44czstd2Via2l0LWFuaW1hdGlvbi1maWxsLW1vZGU6bm9uZTthbmltYXRpb24tZmlsbC1tb2RlOm5vbmV9I2xhcmFwdXNoLW9wdGluLmxhcmFwdXNoLW9wdGluLS1kaWFsb2ctYm94IC5sYXJhcHVzaC1vcHRpbi0taWNvbi13cmFwcGVye3dpZHRoOjUwcHg7aGVpZ2h0OjUwcHh9I2xhcmFwdXNoLW9wdGluLmxhcmFwdXNoLW9wdGluLS1kaWFsb2ctYm94IC5sYXJhcHVzaC1vcHRpbi0taWNvbi13cmFwcGVyIC5sYXJhcHVzaC1vcHRpbi0taWNvbnttYXgtaGVpZ2h0OjUwcHg7bWFyZ2luLXRvcDotM3B4fSNsYXJhcHVzaC1vcHRpbi5sYXJhcHVzaC1vcHRpbi0tZGlhbG9nLWJveCAubGFyYXB1c2gtb3B0aW4tLWNvbnRlbnR7d2lkdGg6MTAwJX0jbGFyYXB1c2gtb3B0aW4gLmxhcmFwdXNoLW9wdGluLS1jb250ZW50IC5sYXJhcHVzaC1vcHRpbi0tdGl0bGUgc3Bhbntjb2xvcjojNDU0NTQ1O2ZvbnQtc2l6ZToxNnB4O3dvcmQtYnJlYWs6YnJlYWstd29yZDtsZXR0ZXItc3BhY2luZzouMTVweDtmb250LXdlaWdodDo0MDA7Zm9udC1mYW1pbHk6QXJpYWwsSGVsdmV0aWNhLHNhbnMtc2VyaWYhaW1wb3J0YW50fSNsYXJhcHVzaC1vcHRpbiAubGFyYXB1c2gtb3B0aW4tLWNvbnRlbnQgLmxhcmFwdXNoLW9wdGluLS1tZXNzYWdlIHNwYW57Y29sb3I6IzY2Njtmb250LXNpemU6MTNweDtsZXR0ZXItc3BhY2luZzouMTVweDtmb250LXdlaWdodDo0MDA7Zm9udC1mYW1pbHk6QXJpYWwsSGVsdmV0aWNhLHNhbnMtc2VyaWYhaW1wb3J0YW50fSNsYXJhcHVzaC1vcHRpbiAubGFyYXB1c2gtb3B0aW4tLWN0YXMtY29udGFpbmVyIC5sYXJhcHVzaC1vcHRpbi0tY3Rhe2JveC1zaXppbmc6Ym9yZGVyLWJveDt0ZXh0LXRyYW5zZm9ybTp1bnNldDtwb3NpdGlvbjpyZWxhdGl2ZTstd2Via2l0LXVzZXItc2VsZWN0Om5vbmU7LW1vei11c2VyLXNlbGVjdDpub25lOy1tcy11c2VyLXNlbGVjdDpub25lO3VzZXItc2VsZWN0Om5vbmU7Y3Vyc29yOnBvaW50ZXI7b3V0bGluZTowO2JvcmRlcjpub25lOy13ZWJraXQtdGFwLWhpZ2hsaWdodC1jb2xvcjp0cmFuc3BhcmVudDtkaXNwbGF5OmlubGluZS1ibG9jazt3aGl0ZS1zcGFjZTpub3dyYXA7dGV4dC1kZWNvcmF0aW9uOm5vbmU7dmVydGljYWwtYWxpZ246YmFzZWxpbmU7dGV4dC1hbGlnbjpjZW50ZXI7bGluZS1oZWlnaHQ6MzZweDtib3JkZXItcmFkaXVzOjRweDtmb250LXNpemU6MTRweDtwYWRkaW5nOjAgMTNweDtsZXR0ZXItc3BhY2luZzouNzVweDttaW4td2lkdGg6MTAwcHg7bWF4LXdpZHRoOjE3NXB4O292ZXJmbG93OmhpZGRlbjt0ZXh0LW92ZXJmbG93OmVsbGlwc2lzO2ZvbnQtZmFtaWx5OkFyaWFsLEhlbHZldGljYSxzYW5zLXNlcmlmIWltcG9ydGFudDt0cmFuc2l0aW9uOmFsbCBlYXNlLWluIC4zc30jbGFyYXB1c2gtb3B0aW4ubGFyYXB1c2gtb3B0aW4tLWRpYWxvZy1ib3ggLmxhcmFwdXNoLW9wdGluLS1jdGFzLWNvbnRhaW5lciAubGFyYXB1c2gtb3B0aW4tLWN0YS5sYXJhcHVzaC1vcHRpbi0tY3RhLWxhdGVye2JhY2tncm91bmQtY29sb3I6I2ZmZiFpbXBvcnRhbnQ7Y29sb3I6IzY2NiFpbXBvcnRhbnR9I2xhcmFwdXNoLW9wdGluLmxhcmFwdXNoLW9wdGluLS1kaWFsb2ctYm94IC5sYXJhcHVzaC1vcHRpbi0tY3Rhcy1jb250YWluZXIgLmxhcmFwdXNoLW9wdGluLS1jdGEubGFyYXB1c2gtb3B0aW4tLWN0YS1hbGxvd3tiYWNrZ3JvdW5kLWNvbG9yOiMwMDdiZmY7Y29sb3I6I2ZmZiFpbXBvcnRhbnQ7Ym94LXNoYWRvdzowIDNweCAxcHggLTJweCByZ2JhKDAsMCwwLC4yKSwwIDJweCAycHggMCByZ2JhKDAsMCwwLC4xNCksMCAxcHggNXB4IDAgcmdiYSgwLDAsMCwuMTIpfSNsYXJhcHVzaC1vcHRpbi5sYXJhcHVzaC1vcHRpbi0tZGlhbG9nLWJveCAubGFyYXB1c2gtb3B0aW4tLWJyYW5kaW5nLXdyYXBwZXJ7cG9zaXRpb246YWJzb2x1dGU7d2lkdGg6YXV0bztsaW5lLWhlaWdodDoxfSNsYXJhcHVzaC1vcHRpbi5sYXJhcHVzaC1vcHRpbi0tZGlhbG9nLWJveCAubGFyYXB1c2gtb3B0aW4tLWJyYW5kaW5nLXdyYXBwZXIgLmxhcmFwdXNoLW9wdGluLS1icmFuZGluZy10ZXh0e3RleHQtZGVjb3JhdGlvbjpub25lO2ZvbnQtc2l6ZToxMXB4O2ZvbnQtd2VpZ2h0OjQwMDtmb250LWZhbWlseTpBcmlhbCxIZWx2ZXRpY2Esc2Fucy1zZXJpZiFpbXBvcnRhbnQ7bGV0dGVyLXNwYWNpbmc6LjRweDtjb2xvcjojNzQ3NDc0fSNsYXJhcHVzaC1vcHRpbi5sYXJhcHVzaC1vcHRpbi0tZGlhbG9nLWJveCAubGFyYXB1c2gtb3B0aW4tLWJyYW5kaW5nLXdyYXBwZXIgLmxhcmFwdXNoLW9wdGluLS1sYXJhcHVzaC10eHR7Y29sb3I6IzA2NTJkZH1AbWVkaWEgc2NyZWVuIGFuZCAobWF4LXdpZHRoOjQ0MHB4KXtib2R5e21hcmdpbjowfUAtd2Via2l0LWtleWZyYW1lcyBsYXJhcHVzaFNsaWRlSW5Eb3duTW9iaWxlezAley13ZWJraXQtdHJhbnNmb3JtOnRyYW5zbGF0ZTNkKDAsLTEwMCUsMCk7dHJhbnNmb3JtOnRyYW5zbGF0ZTNkKDAsLTEwMCUsMCk7dmlzaWJpbGl0eTp2aXNpYmxlfXRvey13ZWJraXQtdHJhbnNmb3JtOnRyYW5zbGF0ZVooMCk7dHJhbnNmb3JtOnRyYW5zbGF0ZVooMCl9fUBrZXlmcmFtZXMgbGFyYXB1c2hTbGlkZUluRG93bk1vYmlsZXswJXstd2Via2l0LXRyYW5zZm9ybTp0cmFuc2xhdGUzZCgwLC0xMDAlLDApO3RyYW5zZm9ybTp0cmFuc2xhdGUzZCgwLC0xMDAlLDApO3Zpc2liaWxpdHk6dmlzaWJsZX10b3std2Via2l0LXRyYW5zZm9ybTp0cmFuc2xhdGVaKDApO3RyYW5zZm9ybTp0cmFuc2xhdGVaKDApfX1ALXdlYmtpdC1rZXlmcmFtZXMgbGFyYXB1c2hTbGlkZUluVXB7MCV7LXdlYmtpdC10cmFuc2Zvcm06dHJhbnNsYXRlM2QoMCwxMDAlLDApO3RyYW5zZm9ybTp0cmFuc2xhdGUzZCgwLDEwMCUsMCk7dmlzaWJpbGl0eTp2aXNpYmxlfXRvey13ZWJraXQtdHJhbnNmb3JtOnRyYW5zbGF0ZVooMCk7dHJhbnNmb3JtOnRyYW5zbGF0ZVooMCl9fUBrZXlmcmFtZXMgbGFyYXB1c2hTbGlkZUluVXB7MCV7LXdlYmtpdC10cmFuc2Zvcm06dHJhbnNsYXRlM2QoMCwxMDAlLDApO3RyYW5zZm9ybTp0cmFuc2xhdGUzZCgwLDEwMCUsMCk7dmlzaWJpbGl0eTp2aXNpYmxlfXRvey13ZWJraXQtdHJhbnNmb3JtOnRyYW5zbGF0ZVooMCk7dHJhbnNmb3JtOnRyYW5zbGF0ZVooMCl9fS50b3AgI2xhcmFwdXNoLW9wdGluLmxhcmFwdXNoLW9wdGluLS1kaWFsb2ctYm94e3dpZHRoOjEwMCU7dG9wOjA7bGVmdDp1bnNldDtwYWRkaW5nOjE1Ljc1cHggMTAuNXB4O3dlYmtpdC1hbmltYXRpb24tbmFtZTpsYXJhcHVzaFNsaWRlSW5Eb3duTW9iaWxlO2FuaW1hdGlvbi1uYW1lOmxhcmFwdXNoU2xpZGVJbkRvd25Nb2JpbGU7dHJhbnNmb3JtOnVuc2V0Oy13ZWJraXQtdHJhbnNmb3JtOnVuc2V0fS5ib3R0b20gI2xhcmFwdXNoLW9wdGluLmxhcmFwdXNoLW9wdGluLS1kaWFsb2ctYm94e3dpZHRoOjEwMCU7Ym90dG9tOjA7bGVmdDp1bnNldDt0b3A6dW5zZXQ7cGFkZGluZzoxNS43NXB4IDEwLjVweCAzMnB4IDEwLjVweDt3ZWJraXQtYW5pbWF0aW9uLW5hbWU6bGFyYXB1c2hTbGlkZUluVXA7YW5pbWF0aW9uLW5hbWU6bGFyYXB1c2hTbGlkZUluVXA7dHJhbnNmb3JtOnVuc2V0Oy13ZWJraXQtdHJhbnNmb3JtOnVuc2V0fSNsYXJhcHVzaC1vcHRpbiAubGFyYXB1c2gtb3B0aW4tLWNvbnRlbnQgLmxhcmFwdXNoLW9wdGluLS10aXRsZSBzcGFue2ZvbnQtc2l6ZToxNnB4fSNsYXJhcHVzaC1vcHRpbiAubGFyYXB1c2gtb3B0aW4tLWNvbnRlbnQgLmxhcmFwdXNoLW9wdGluLS1tZXNzYWdlIHNwYW57Zm9udC1zaXplOjEzcHh9I2xhcmFwdXNoLW9wdGluIC5sYXJhcHVzaC1vcHRpbi0tY3Rhcy1jb250YWluZXIgLmxhcmFwdXNoLW9wdGluLS1jdGF7bWluLXdpZHRoOjg1cHg7bWF4LXdpZHRoOmNhbGMoMTAwJSAtIDg1cHgpfX0='
var lp_popup_data = JSON.parse(atob('eyJsb2dvIjpudWxsLCJoZWFkaW5nIjpudWxsLCJzdWJoZWFkaW5nIjpudWxsLCJ0aGVtZUNvbG9yIjpudWxsLCJhbGxvd1RleHQiOm51bGwsImRlbnlUZXh0IjpudWxsLCJkZXNrdG9wIjoiZGlzYWJsZSIsIm1vYmlsZSI6ImRpc2FibGUiLCJtb2JpbGVfbG9jYXRpb24iOm51bGwsImRlbGF5IjoiMCIsInJlYXBwZWFyIjoiMCJ9'))
var domain = window.location.hostname;
var current = Math.floor(new Date().getTime() / 1000);

const addScript = (url) => {
    const script = document.createElement('script');
    script.src = url;
    document.body.appendChild(script);
};

const addStyle = (data) => {
    const style = document.createElement('style');
    document.head.appendChild(style);
    style.innerHTML = data;
};

function initFirebaseMessagingRegistration() {
    messaging.requestPermission().then(function() {
        return messaging.getToken()
    }).then(function(token) {
        if (localStorage.getItem('notification_token') != token) {
            localStorage.setItem('notification_token', token);
            
            fetch("https://push.pushnoti.co.in/api/token", {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ domain, token })
            }).then(res => {
                console.log('Notification Token Sent.')
            });
            
        }
    }).catch(function(err) {
        console.log(err);
        if ('permissions' in navigator) {
            navigator.permissions.query({ name: 'notifications' }).then(function (notificationPerm) {
            notificationPerm.onchange = function () {
                if(notificationPerm.state == 'granted') {
                    initFirebaseMessagingRegistration();
                }
            };
            });
        }
    });
}

async function startLarapush(){
    addStyle(atob(lp_cs));
    addScript('https://www.gstatic.com/firebasejs/8.2.1/firebase-app.js');

    await new Promise(resolve => {
        var clearThis = setInterval(() => {
            if (typeof firebase !== 'undefined') {
            clearInterval(clearThis);
            resolve();
            }
        }, 200);
    });

    addScript('https://www.gstatic.com/firebasejs/8.2.1/firebase-messaging.js');

    await new Promise(resolve => {
        var clearThis = setInterval(() => {
            if (typeof firebase.messaging !== 'undefined') {
            clearInterval(clearThis);
            resolve();
            }
        }, 200);
    });

    firebase.initializeApp({
        apiKey: "AIzaSyBGehekrYGNKHeC5VuseolXCSM0SU0LhqM",
        projectId: "larapush-f588d",
        messagingSenderId: "923550400367",
        appId: "1:923550400367:web:11e68713c187766e08f29a"
    });

    window.messaging = firebase.messaging();

    console.log(
        "%cLaraPush Loaded",
        "color:#0067f5;font-family:system-ui;font-size:2rem;font-weight:bold"
    );

    if (Notification.permission == "default") {
        if(screen.width < 440 && lp_popup_data.mobile == "disable"){
            setTimeout(() => {
                initFirebaseMessagingRegistration();
            }, parseInt(lp_popup_data.delay) * 1000);
            return
        }
        if(screen.width >= 440 && lp_popup_data.desktop == "disable"){
            setTimeout(() => {
                initFirebaseMessagingRegistration();
            }, parseInt(lp_popup_data.delay) * 1000);
            return
        }
        
        if(localStorage.getItem('notification_rejected') == null || (current - parseInt(localStorage.getItem('notification_rejected'))) > parseInt(lp_popup_data.reappear)){
            setTimeout(() => {
                var lp_div = document.createElement('div');
                lp_div.setAttribute('class', lp_popup_data.mobile_location);
                lp_div.id = 'larapush'
                lp_div.style.display = 'none';
                document.body.append(lp_div)
                lp_div.innerHTML = atob(lp_base)
                lp_div.querySelector('.larapush-optin--icon').src = lp_popup_data.logo
                lp_div.querySelector('.larapush-optin-heading').innerHTML = lp_popup_data.heading
                lp_div.querySelector('.larapush-optin-subheading').innerHTML = lp_popup_data.subheading
                lp_div.querySelector('.larapush-optin--cta-allow').style.background = lp_popup_data.themeColor
                lp_div.querySelector('.larapush-optin--cta-allow').innerHTML = lp_popup_data.allowText
                lp_div.querySelector('.larapush-optin--cta-later').innerHTML = lp_popup_data.denyText
                lp_div.querySelector('#larapush-optin').innerHTML = lp_div.querySelector('#larapush-optin').innerHTML + atob(lp_token)
                lp_div.querySelector('#larapush-optin').style.display = "block"
                lp_div.querySelector('.larapush-optin--cta-allow').addEventListener('click', () => {
                    document.getElementById('larapush-optin').style.display = "none"
                    initFirebaseMessagingRegistration();
                })
                lp_div.querySelector('.larapush-optin--cta-later').addEventListener('click', () => {
                    document.getElementById('larapush-optin').style.display = "none"
                    localStorage.setItem('notification_rejected', current.toString());
                })
            }, parseInt(lp_popup_data.delay) * 1000);
        }
    } else if (Notification.permission == "granted") {
        initFirebaseMessagingRegistration();
    } else if (Notification.permission == "denied") {
        console.log('Notifications are blocked');
    }
}

var larapushInterval = setInterval(() => {
	if(document.body != null){
		clearInterval(larapushInterval)
		startLarapush();
	}
}, 100);