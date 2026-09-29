// Client Script for Project DocType
frappe.ui.form.on('Project', {
	status(frm) {
		if (frm.doc.status === 'Completed') {
			show_closure_dialog(frm);
		}
	}
});

function show_closure_dialog(frm) {
	const existing_metrics = frm.doc.custom_impact_metrics || '';
	const existing_summary = frm.doc.custom_closure_summary || '';

	const d = new frappe.ui.Dialog({
		title: __('Project Closure — Required Information'),
		fields: [
			{
				fieldtype: 'HTML',
				options: `<p style="color:#854F0B;font-size:12px;margin-bottom:8px;">
					⚠ Both fields are mandatory before this project can be marked as Closed.
				</p>`
			},
			{
				label: __('Impact Metrics'),
				fieldname: 'impact_metrics',
				fieldtype: 'Text Editor',
				reqd: 1,
				default: existing_metrics,
				description: __('Beneficiaries reached, outputs delivered, SDG indicators')
			},
			{
				label: __('Closure Summary'),
				fieldname: 'closure_summary',
				fieldtype: 'Text Editor',
				reqd: 1,
				default: existing_summary,
				description: __('Key achievements, challenges, lessons learned, budget notes')
			}
		],
		primary_action_label: __('Save & Close Project'),
		primary_action(values) {
			if (!values.impact_metrics || !values.impact_metrics.trim()) {
				frappe.msgprint({
					message: __('Impact Metrics is required to close the project.'),
					indicator: 'red',
					title: __('Required')
				});
				return;
			}
			if (!values.closure_summary || !values.closure_summary.trim()) {
				frappe.msgprint({
					message: __('Closure Summary is required to close the project.'),
					indicator: 'red',
					title: __('Required')
				});
				return;
			}

			frm.set_value('custom_impact_metrics', values.impact_metrics);
			frm.set_value('custom_closure_summary', values.closure_summary);
			frm.set_value('custom_project_phase', 'Closed');

			d.hide();

			frm.save().then(() => {
				frappe.show_alert({
					message: __('✅ Project closed successfully with closure data saved.'),
					indicator: 'green'
				}, 5);
				frm.reload_doc();
			});
		},
		secondary_action_label: __('Cancel'),
		secondary_action() {
			frm.set_value('status', 'Open');
			d.hide();
			frappe.show_alert({
				message: __('Project status reverted to Open. Fill closure data to proceed.'),
				indicator: 'orange'
			}, 4);
		}
	});

	d.show();
}
