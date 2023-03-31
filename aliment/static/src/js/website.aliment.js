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

                //Liste Aliment
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
                ev.preventDefault();

                var name = $('#name').val();

                ajax.jsonRpc('/creer_alliment', 'call', {
                  'name': name,
                }).then(function (result) {
                  location.reload();
                });
                });

                //Modifier
                var ajax = require('web.ajax');

                $('#modifier').on('submit', function (ev) {
                ev.preventDefault();

                var new_id = $('#new_id').val();
                var new_name = $('#new_name').val();
                ajax.jsonRpc('/modifier_aliment', 'call', {
                    'new_id': new_id,
                    'new_name': new_name
                }).then(function (result) {
                  location.reload();
                });
                });

                //Delete
                var ajax = require('web.ajax');

                $('#supprimer').on('submit', function (ev) {
                ev.preventDefault();

                var old_id = $('#old_id').val();
                ajax.jsonRpc('/delete_aliment', 'call', {
                    'old_id': old_id,
                }).then(function (result) {
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
