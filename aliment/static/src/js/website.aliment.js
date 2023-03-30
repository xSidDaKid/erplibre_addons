odoo.define("aliment.animation",
function (require) {
    "use strict";

    let sAnimation = require("website.content.snippets.animation");

    sAnimation.registry.aliment =
        sAnimation.Class.extend({
            selector: ".o_aliment",

            start: function () {
                let self = this;
                this._eventList = this.$(".aliment_value");
                this._originalContent = this._eventList.text();
                //this._originalContent = this._eventList[0].outerHTML;

                let def = this._rpc({
                    route: "/listeAliment",
                }).then(function (data) {
                    if (data.error) {
                        return;
                    }

                    if (_.isEmpty(data)) {
                        return;
                    }
                    var list = $("<ul>");
                    _.each(data.aliments, function (item) {
                        //list.append($("<li>").text(item));
                        var listItem = $("<li>");
                        var itemText = " (ID: " + item.id + ") " + item.name;
                        listItem.text(itemText);
                        list.append(listItem);
                    });

                self._eventList.html(list);
                });

                //Création
                var ajax = require('web.ajax');

                $('#creer').on('submit', function (ev) {
                ev.preventDefault();  // prevent default form submission behavior

                var name = $('#name').val();

                ajax.jsonRpc('/creer_alliment', 'call', {
                  'name': name,
                }).then(function (result) {
                  // handle the result of the RPC call here
                  console.log(result);
                  location.reload();
                });
                });

                //Modifier

                var ajax = require('web.ajax');

                $('#modifier').on('submit', function (ev) {
                ev.preventDefault();  // prevent default form submission behavior

                var new_id = $('#new_id').val();
                var new_name = $('#new_name').val();
                console.log("id: = "+id+"/name: "+new_name);
                ajax.jsonRpc('/modifier_aliment', 'call', {
                    'new_id': new_id,
                    'new_name': new_name
                }).then(function (result) {
                  // handle the result of the RPC call here
                  console.log(result);
                  location.reload();
                });
                });


                return $.when(this._super.apply(this, arguments), def);
            },
            destroy: function () {
                this._super.apply(this, arguments);
                if (this._$loadedContent) {
                    this._eventList.text(this._originalContent);
                }
            },
        });
});
