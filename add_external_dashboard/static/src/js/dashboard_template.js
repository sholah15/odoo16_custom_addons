/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

class LookerStudio extends Component {
    setup() {
        this.url = useState({ value: "" });
        this.orm = useService("orm");
        this.endLoading = useState({ value: false });
        this.getDashboardURL();
    }

    async getDashboardURL() {
        try {
            const data = await this.orm.call("update.looker", "get_URL", [{}]);
            this.url.value = data;
        } catch (error) {
            console.error("Error fetching dashboard URL:", error);
        } finally {
            this.endLoading.value = true;
        }
    }
}

LookerStudio.template = "looker_studio.dashboardtemplate";

// Daftarkan komponen dalam registry Odoo
registry.category("actions").add("looker_studio.LookerStudio", LookerStudio);