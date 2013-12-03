var geocoder = 'vacio';

function geocodificar(event){
	if(event.keyCode == 13){
		alert("geocode: " + event.srcElement.value);
		if(geocoder == 'vacio'){
			geocoder = new google.maps.Geocoder();

			OpenLayers.Control.prototype.keepEvents = function(div) {
			    this.keepEventsDiv = new OpenLayers.Events(this, div, null, true);
			    // IN THIS CASE triggerButton IS NOT NECESSARY 
			    var triggerButton = function (evt) { 
			        var element = OpenLayers.Event.element(evt),
			            buttonclick = map_ubicacion.map.events && 
			                    map_ubicacion.map.events.extensions && 
			                    map_ubicacion.map.events.extensions.buttonclick;        
			        if (element && buttonclick) {
			            element = buttonclick.getPressedButton(element);
			            if (element && OpenLayers.Element.hasClass(element, "olButton")) {
			                buttonclick.buttonClick(evt);
			            }
			        }
			    };
			    var listeners = {
			        "mousedown": function (evt) {
			            this.mousedown = true;
			            triggerButton(evt);
			            OpenLayers.Event.stop(evt, true);
			        },
			        "mousemove": function (evt) {
			            if (this.mousedown) {
			                OpenLayers.Event.stop(evt, true);
			            }
			        },
			        "mouseup": function (evt) {
			            if (this.mousedown) {
			                this.mousedown = false;
			                triggerButton(evt);
			                OpenLayers.Event.stop(evt, true);
			            }
			        },
			        "click": function (evt) {
			            var element = OpenLayers.Event.element(evt);
			            triggerButton(evt);
			            OpenLayers.Event.stop(evt, true);
			        },
			        "mouseout": function (evt) {
			            this.mousedown = false;
			        },
			        "dblclick": function (evt) {
			            var element = OpenLayers.Event.element(evt);
			            triggerButton(evt);
			            OpenLayers.Event.stop(evt, true);
			        },
			        "touchstart": function (evt) {
			            OpenLayers.Event.stop(evt, true);
			        },
			        scope: this
			    };
			    this.keepEventsDiv.on(listeners);
			};

			var customControl = OpenLayers.Class(OpenLayers.Control, {
			    initialize : function() {
			        OpenLayers.Control.prototype.initialize.apply(this, arguments);
			    },
			    draw: function () {
			        var div = OpenLayers.Control.prototype.draw.apply(this, arguments);
			        var html = "<div><input type='text' id='textToolbar' value='This not work..'/></div>";
			        div.innerHTML = html;
			        this.keepEvents(div);
			        return div;
			    },
			    allowSelection: true // REQUIRED!    
			});
			
			map_ubicacion.map.addControl(new customControl());			
		}
		geocoder.geocode( { 'address': event.srcElement.value}, function(results, status) {
			if (status == google.maps.GeocoderStatus.OK) {
				alert(results[0].geometry.location);
				var lat = results[0].geometry.location.lat();
				var lng = results[0].geometry.location.lng();
				var centro = new OpenLayers.LonLat(lng,lat);
				var prj_dest = new OpenLayers.Projection("EPSG:900913");
				var prj_orig = new OpenLayers.Projection("EPSG:4326");
				map_ubicacion.map.setCenter(centro.transform(prj_orig,prj_dest));
			} else {
	        	alert("Geocode was not successful for the following reason: " + status);
			}
		});
		return false;
	}else{
		return true;
	}
};