odoo.define("aliment.animation",
function (require) {
    "use strict";

    let sAnimation = require("website.content.snippets.animation");
    const ajax = require('web.ajax');

    sAnimation.registry.aliment = sAnimation.Class.extend({
		selector: ".o_aliment",
		read_events: {
		  'submit #creer': '_creerAliment',
		  'submit #modifier': '_modifierAliment',
		  'submit #supprimer': '_supprimerAliment',
		},
		handleSubmit: function (endpoint, data, form) {
			ajax.jsonRpc(endpoint, 'call', data).then(function (result) {
				form[0].reset();
				location.reload();
			});
		},
		_creerAliment: function (event) {
			event.preventDefault();
			let name = this.$('#name').val();
			this.handleSubmit('/creer_alliment', {'name': name,}, $(event.currentTarget));
		},
		_modifierAliment: function (event) {
			event.preventDefault();
			let new_id = this.$('#new_id').val();
			let new_name = this.$('#new_name').val();
			this.handleSubmit('/modifier_aliment', {'new_id': new_id, 'new_name': new_name}, $(event.currentTarget));
		},
		_supprimerAliment: function (event) {
			event.preventDefault();
			let old_id = this.$('#old_id').val();
			this.handleSubmit('/delete_aliment', {'old_id': old_id}, $(event.currentTarget));
		},

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
