odoo.define('point_of_sale_extension.Orderline', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');

    class Orderline extends PosComponent {
        selectLine() {
            var session = require('web.session');
            session['product_id'] = this.props.line.product.id
            this.trigger('select-line', { orderline: this.props.line });
        }
        lotIconClicked() {
            var session = require('web.session');
            session['product_id'] = this.props.line.product.id
            this.trigger('edit-pack-lot-lines', { orderline: this.props.line });
        }
        get addedClasses() {
            return {
                selected: this.props.line.selected,
            };
        }
        get customerNote() {
            return this.props.line.get_customer_note();
        }
    }
    Orderline.template = 'Orderline';

    Registries.Component.add(Orderline);

    return Orderline;
});
