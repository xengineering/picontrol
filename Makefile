
.PHONY: install uninstall

install :
	install -Dm 644 "main.py" "/usr/share/eu.xengineering.picontrol/main.py"
	install -Dm 644 "picontrol.service" "/usr/lib/systemd/system/picontrol.service"
	install -Dm 644 "static/css/style.css" "/usr/share/eu.xengineering.picontrol/static/css/style.css"
	install -Dm 644 "static/img/favicon.ico" "/usr/share/eu.xengineering.picontrol/static/img/favicon.ico"
	install -Dm 644 "static/js/api_client.js" "/usr/share/eu.xengineering.picontrol/static/js/api_client.js"
	install -Dm 644 "templates/index.html" "/usr/share/eu.xengineering.picontrol/templates/index.html"

uninstall :
	rm -f /usr/lib/systemd/system/picontrol.service
	rm -rf /usr/share/eu.xengineering.picontrol/
