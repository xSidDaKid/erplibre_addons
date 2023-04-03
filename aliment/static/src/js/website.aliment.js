odoo.define("aliment.animation",
function (require) {
    "use strict";

    let sAnimation = require("website.content.snippets.animation");
    const ajax = require('web.ajax');

    sAnimation.registry.aliment =
        sAnimation.Class.extend({
            selector: ".o_aliment",
/*            read_events: {
              //'submit #creer': '_toggleForm',
            },

            _toggleForm: function (event) {
                let self = this;
                event.preventDefault();
                event.stopPropagation();

                let result = self._onChangeConfigStep(event, false);
                if (result) {
                    result.then(function (data) {
                        if (data) {
                            if (data.next_step) {
                                self._openNextStep(data.next_step);
                            };
                            if (data.redirect_url) {
                                window.location = data.redirect_url;
                            };
                        };
                    });
                }
            },*/

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

                    let list = $("<ul>");
                    _.each(data.aliments, function (item) {
                        let listItem = $("<li>");
                        let itemText = " (ID: " + item.id + ") " + item.name;
                        listItem.text(itemText);
                        list.append(listItem);
                    });
                    self._eventList.html(list);
                });

                const handleSubmit = (endpoint, data, form) => {
                    ajax.jsonRpc(endpoint, 'call', data).then(function (result) {
                        form[0].reset();
                        location.reload();
                    });
                };

                //Création
                this.$('#creer').on('submit', function (ev) {
                    ev.preventDefault();
                    let name = $('#name').val();
                    handleSubmit('/creer_alliment', {'name': name,}, $(this))
                });

                //Modifier
                this.$('#modifier').on('submit', function (ev) {
                    ev.preventDefault();
                    let new_id = $('#new_id').val();
                    let new_name = $('#new_name').val();
                    handleSubmit('/modifier_aliment', {'new_id': new_id, 'new_name': new_name}, $(this))
                });

                //Delete
                this.$('#supprimer').on('submit', function (ev) {
                    ev.preventDefault();
                    let old_id = $('#old_id').val();
                    handleSubmit('/delete_aliment', {'old_id': old_id}, $(this))
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
