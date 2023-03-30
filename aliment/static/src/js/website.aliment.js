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
                //this._originalContent = this._eventList.text();
                this._originalContent = this._eventList[0].outerHTML;

                let def = this._rpc({
                    route: "/listeAliment",
                }).then(function (data) {
                    if (data.error) {
                        return;
                    }

                    if (_.isEmpty(data)) {
                        return;
                    }

                    self._$loadedContent = $(data);
                    //self._eventList.text(data["aliments"]);
                    self._eventList.replaceWith(self._$loadedContent);
                });

                var ajax = require('web.ajax');

                $('#my-form').on('submit', function (ev) {
                ev.preventDefault();  // prevent default form submission behavior

                var name = $('#name').val();

                ajax.jsonRpc('/creer_alliment', 'call', {
                  'name': name,
                }).then(function (result) {
                  // handle the result of the RPC call here
                  console.log(result);
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
