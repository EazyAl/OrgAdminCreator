import meraki
import pprint

API_KEY = ''

dashboard = meraki.DashboardAPI(API_KEY)

orgs = dashboard.organizations.getOrganizations()

email = input("Enter Admin Email: ")
name = input("Enter Admin Name: ")

access = 'read-only'

missed_orgs = []

org_count = 0

for o in range(len(orgs)):

    try:
         pprint.pprint(orgs[o]['name'])

         dashboard.organizations.createOrganizationAdmin(
             orgs[o]['id'], email, name, access,
         )

         org_count = org_count + 1

     except meraki.APIError as e:

        missed_orgs.append(orgs[o]['name'])


if not missed_orgs:
    print("Admin successfully added to all " + org count + " orgs ")

else:
    print("Admin was not added to the following orgs")
    print(missed_orgs)
    print("Admin added to" + org count + " orgs ")
