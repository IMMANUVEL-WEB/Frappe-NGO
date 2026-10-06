frappe.ui.form.on('Volunteer Attendance', {
    in_time: function(frm) {
        calculate_hours(frm);
    },
    out_time: function(frm) {
        calculate_hours(frm);
    }
});

function calculate_hours(frm) {
    if (frm.doc.in_time && frm.doc.out_time) {
        var in_time = moment(frm.doc.in_time, 'HH:mm:ss');
        var out_time = moment(frm.doc.out_time, 'HH:mm:ss');
        var duration = moment.duration(out_time.diff(in_time));
        var hours = duration.asHours();
        
        if (hours > 0) {
            frm.set_value('total_hours', parseFloat(hours.toFixed(2)));
        } else {
            frm.set_value('total_hours', 0);
        }
    }
}
