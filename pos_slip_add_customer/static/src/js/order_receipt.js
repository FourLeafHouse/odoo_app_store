import { OrderReceipt } from "@point_of_sale/app/screens/receipt_screen/receipt/order_receipt";
import { patch } from "@web/core/utils/patch";

patch(OrderReceipt.prototype, "pos_custom_receipt.OrderReceipt", {
    /**
     * Override the setup method to add custom logic.
     */
    setup() {
        this._super.apply(this, arguments);
    },

    /**
     * Get the customer (partner) information from the order.
     * @returns {Object} The customer object.
     */
    get customer() {
        return this.props.data.order.partner;
    },
});