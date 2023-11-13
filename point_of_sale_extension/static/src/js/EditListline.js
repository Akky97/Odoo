odoo.define('point_of_sale_extension.EditListInput', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');
    var rpc = require('web.rpc');
    class EditListInput extends PosComponent {
        onKeyup(event) {
            if (event.key === "Enter" && event.target.value.trim() !== '') {
                this.trigger('create-new-item');
            }
        }

        on_change_key(event){
            var session = require('web.session');
            var res = rpc.query({
                model: 'pos.order',
                method: 'get_lot_available',
                args:[[], this.props.item.text, session.product_id]
            }).then(function (data){
                if (!data){
                    event.target.style.border = "1px solid red"
                }
                else{
                    event.target.style.border = "1px solid rgb(220,220,220)"
                }
            });
            }

    }
    EditListInput.template = 'EditListInput';

    Registries.Component.add(EditListInput);

    return EditListInput;
});
