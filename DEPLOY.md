# Deploying the Organization/Department customizations to production

This app adds an `Organization` and `Department` master list, links them onto
the core `User` and `LMS Course` doctypes, and adds an Organization
breakdown to the LMS course Dashboard tab. The Dashboard breakdown and the
Members-popup fields also required small edits inside the `lms` app itself
(no plugin system exists there for a separate app to inject UI), tracked in
a fork: [attanoorshah/lms](https://github.com/attanoorshah/lms), branch
`ns-customizations-v2.62.1`.

Run the following on the production bench.

## 1. Install this app (first time only)

```bash
cd /path/to/frappe-bench
bench get-app https://github.com/attanoorshah/ns_lms_customizations.git --branch main
bench --site <production-site> install-app ns_lms_customizations
```

## 2. Point the existing `lms` app at the fork branch

This does **not** touch installed data or the database — it only swaps the
git remote/branch of the existing `apps/lms` checkout, so no
`bench remove-app` / `uninstall-app` is involved:

```bash
cd apps/lms
git remote add origin git@github.com:attanoorshah/lms.git   # keep upstream (frappe/lms) as-is
git fetch origin
git checkout -b ns-customizations-v2.62.1 origin/ns-customizations-v2.62.1
cd ../..
```

If `apps/lms` already has local uncommitted changes on production, stash or
commit them first — `git checkout -b` will refuse to run over a dirty tree
that conflicts with the incoming branch.

## 3. Apply everything

```bash
bench --site <production-site> migrate
bench build --app lms --app ns_lms_customizations
bench --site <production-site> clear-cache
```

`migrate` syncs the new `Organization`/`Department` doctypes, runs the
one-time patch that creates the `Organization`/`Department` Custom Fields
and the Members-form Client Script, and replays the fixtures. `bench build`
ships the updated LMS frontend bundle (Members popup + course Dashboard).

## 4. Restart

```bash
sudo supervisorctl status                # confirm the actual program group names on this box
sudo supervisorctl restart <web group>: <workers group>:
```

## Verification after deploy

1. `bench --site <production-site> list-apps` shows `ns_lms_customizations`.
2. Desk → User → a test user shows the "Organization Details" section
   (Organization + Department) in the "More Information" tab.
3. Desk → LMS Course shows an "Organization" field right after "Category".
4. LMS portal → Settings → Users → Add/Edit member shows Organization and
   Department pickers, with Department filtered by the selected Organization.
5. A course's Dashboard tab shows the "Enrollments by Organization" card,
   and clicking a row opens the member drill-down dialog.
