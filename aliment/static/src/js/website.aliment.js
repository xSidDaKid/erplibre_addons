odoo.define("aliment.animation",
function (require) {
    "use strict";

    let sAnimation = require("website.content.snippets.animation");
    const ajax = require('web.ajax');

    sAnimation.registry.aliment =
        sAnimation.Class.extend({
            selector: ".o_aliment",

            start: function () {
                let self = this;
                this._eventList = this.$(".aliment_value");
                this._originalContent = this._eventList.text();

                //Liste Aliment
                let def = this._rpc({
                    route: "/listeAliment",
                }).then(function (data) {
                    if (data.error || _.isEmpty(data)) {
                        return;
                    }

                    var list = $("<ul>");
                    _.each(data.aliments, function (item) {
                        var listItem = $("<li>");
                        var itemText = " (ID: " + item.id + ") " + item.name;
                        listItem.text(itemText);
                        list.append(listItem);
                    });
                    self._eventList.html(list);
                });

                const handleSubmit = (endpoint, data) => {
                    ajax.jsonRpc(endpoint, 'call', data).then(function (result) {
                        location.reload();
                    });
                };

                //Création
                $('#creer').on('submit', function (ev) {
                    ev.preventDefault();
                    var name = $('#name').val();
                    handleSubmit('/creer_alliment', {'name': name,})
                });

                //Modifier
                $('#modifier').on('submit', function (ev) {
                    ev.preventDefault();
                    var new_id = $('#new_id').val();
                    var new_name = $('#new_name').val();
                    handleSubmit('/modifier_aliment', {'new_id': new_id, 'new_name': new_name})
                });

                //Delete
                $('#supprimer').on('submit', function (ev) {
                    ev.preventDefault();
                    var old_id = $('#old_id').val();
                    handleSubmit('/delete_aliment', {'old_id': old_id})
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
