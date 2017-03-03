**Clearview Phase 1 Task List**

*// TODO*
* Clients
    * Validate client model completeness
    * Get form presentation
        * Add + Edit
    * Add view logic
* Employees
    * First design user sign-up
        * Manager sends email invites with company PIN
        * sign up page requiring valid PIN
        * email address as username
    * Then employee model
* Interactions
    * Employee <--> Client

* Implement the remaining models
  * Develop tests for validity, longevity
* Determine contingency for cases where objects are deleted but referenced elsewhere
  * i.e. product is no longer carried but needs to be referenced for all prior interactions/sales
