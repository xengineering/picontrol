

/*
    picontrol - A small Web Application to shutdown or reboot your Raspberry Pi.

    Copyright (C) 2020  xengineering

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/


function poweroff() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/api", true);
    xhr.setRequestHeader("Content-type", "application/json");
    var data = {"cmd":"poweroff"}
    var json = JSON.stringify(data);
    xhr.send(json);
}


function reboot() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/api", true);
    xhr.setRequestHeader("Content-type", "application/json");
    var data = {"cmd":"reboot"}
    var json = JSON.stringify(data);
    xhr.send(json);
}
