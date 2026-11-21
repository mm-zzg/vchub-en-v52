# Constraints & Tasks

Use the **Constraints & Tasks** page to create and manage constraints and scheduled tasks.

To add a constraint, open **Constraints & Tasks** and click the first **Add** button.

![alt text](c1.png)

The page provides two constraint types: **Grid Setpoint Change Constraint** and **Charging Restricted Constraint**.

![alt text](c2.png)

## Grid Setpoint Change Constraint

This constraint temporarily changes the predefined **15-Minute Mean Active Power** setpoint at the configured time.

![alt text](c3.png)

After configuring the constraint, click **Add** button and confirm the upcoming setpoint change in prompt.

![alt text](c4.png)

When the local time falls within the configured effective period, the constraint is shown with a highlighted green border.

![alt text](c5.png)

Click Peak Load Management sidebar button, click Configuration Settings tab, users can view the configured setpoint constraints.

![alt text](c6.png)

After 15 minutes, the setpoint automatically changes to the configured value.

![alt text](c7.png)

User can modify constraint by clicking its **Edit** button. User can update the setpoint, upper threshold, lower threshold, start time, end time, effective time period start time,  effective time period end time and status.

![alt text](c8.png) 

![alt text](c11.png)

The constraint information displayed on the page will update to reflect modified changes.

![alt text](c12.png)

User can disable constraint's status or change effective time to cancel the constraint.

![alt text](c9.png)

If only change the effective time and enable the constraint, its text is displayed in black font.

![alt text](c13.png)

![alt text](c14.png)

If disable the constraint, the highlighted green border disappears and the constraint is displayed in gray font.

![alt text](c10.png)

User can delete a constraint only after disabling it.

![alt text](c15.png)

## Charging Restricted Constraint

The Charging Restricted Constraint prevents the selected battery storage from charging at any time.

Only controllable battery storage systems are available in the selection list. Uncontrollable systems cannot be selected.

![alt text](c16.png)

After clicking **Add** button, the constraint and its related information are displayed on the page.

![alt text](c17.png)

While this constraint is enabled, the selected battery storage systems cannot charge using grid power.

Select **Edit** to modify the Charging Restricted Constraint.

![alt text](c18.png)

The editing and deletion rules are the same as those for the Grid Setpoint Change Constraint: disable the constraint before deleting it.

## Tasks

To add a task, open **Constraints & Tasks** and select the second **Add** button.

![alt text](c19.png)

Only controllable battery storage systems are available in the selection list. Uncontrollable systems cannot be selected.

![alt text](c20.png)

When no constraints or Peak Load limits prevent operation, a task can automatically charge the selected battery storage at the scheduled time.

The editing and deletion rules are the same as those for the Grid Setpoint Change Constraint.

## Filter Constraints and Tasks

Use the filter controls to narrow constraints and tasks by type, selected components, weekdays, time, or action.

![alt text](c21.png)

After selecting a filter condition, matching results are displayed and the selected condition is highlighted.

![alt text](c22.png)

Select active filter condition again could clear that filter.

![alt text](c23.png)

User can open the **Overview Components** tab to view all constraints and tasks.

![alt text](c25.png)

System can filter the applied components by selecting  **Component Type** and  **Component**.

![alt text](c24.png)

The selected components will display here.

![alt text](c26.png)

User can select a filter tab to create filter conditions.

![alt text](c27.png)

Matching results will be displayed after selecting, and the selected filter condition is highlighted.

![alt text](c28.png)

User can click active filter condition again to clear or change filter conditions.

![alt text](c29.png)

User can click **Clear** button to remove the component filter.

![alt text](c30.png)

![alt text](c31.png)