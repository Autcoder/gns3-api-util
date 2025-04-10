import time
from gns3util.get import GNS3APIClient

# Define ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Create a dummy subclass to override _api_call and _stream_notifications for testing
class DummyGNS3APIClient(GNS3APIClient):
    def _api_call(self, endpoint, stream=False, method="GET", data=None):
        # Return a dummy response based on endpoint
        return (True, f"Dummy response for {endpoint}")

    def _stream_notifications(self, endpoint, timeout_seconds=60):
        print(f"Dummy notification stream for {endpoint}")
        time.sleep(0.1)

def run_test(description, func, expected=None):
    print(f"Testing {description}...", end=" ")
    try:
        result = func()
        if expected is not None:
            if result == expected:
                print(f"{GREEN}Success{RESET}")
            else:
                print(f"{RED}Failed: Expected '{expected}', got '{result}'{RESET}")
        else:
            # No expected output provided; test passed if no exception was raised.
            print(f"{GREEN}Success{RESET}")
    except Exception as e:
        print(f"{RED}Failed: Exception {e}{RESET}")

def main():
    client = DummyGNS3APIClient("http://dummy")

    # Define tests as a list of (description, lambda for function call, expected output)
    tests = [
        # Zero argument methods
        ("version", lambda: client.version()[1], "Dummy response for version"),
        ("iou_license", lambda: client.iou_license()[1], "Dummy response for iou_license"),
        ("statistics", lambda: client.statistics()[1], "Dummy response for statistics"),
        ("me", lambda: client.current_user_info()[1], "Dummy response for access/users/me"),
        ("users", lambda: client.users()[1], "Dummy response for access/users"),
        ("projects", lambda: client.projects()[1], "Dummy response for projects"),
        ("groups", lambda: client.groups()[1], "Dummy response for access/groups"),
        ("roles", lambda: client.roles()[1], "Dummy response for access/roles"),
        ("privileges", lambda: client.privileges()[1], "Dummy response for access/privileges"),
        ("acl-endpoints", lambda: client.aclEndpoints()[1], "Dummy response for access/acl/endpoints"),
        ("acl", lambda: client.acl()[1], "Dummy response for access/acl"),
        ("templates", lambda: client.templates()[1], "Dummy response for templates"),
        ("symbols", lambda: client.symbols()[1], "Dummy response for symbols"),
        ("default-symbols", lambda: client.defaultSymbols()[1], "Dummy response for symbols/default_symbols"),
        ("computes", lambda: client.computes()[1], "Dummy response for computes"),
        ("appliances", lambda: client.appliances()[1], "Dummy response for appliances"),
        ("pools", lambda: client.pools()[1], "Dummy response for pools"),

        # One-argument methods
        ("user", lambda: client.user("user1")[1], "Dummy response for access/users/user1"),
        ("user-groups", lambda: client.users_groups("user1")[1], "Dummy response for access/users/user1/groups"),
        ("project", lambda: client.project("proj1")[1], "Dummy response for projects/proj1"),
        ("project-stats", lambda: client.project_stats("proj1")[1], "Dummy response for projects/proj1/stats"),
        ("project-locked", lambda: client.project_locked("proj1")[1], "Dummy response for projects/proj1/locked"),
        ("group", lambda: client.groupsById("group1")[1], "Dummy response for access/groups/group1"),
        ("group-members", lambda: client.groupMembers("group1")[1], "Dummy response for access/groups/group1/members"),
        ("role", lambda: client.roleById("role1")[1], "Dummy response for access/roles/role1"),
        ("role-privileges", lambda: client.rolePrivileges("role1")[1], "Dummy response for access/roles/role1/privileges"),
        ("template", lambda: client.templateByID("temp1")[1], "Dummy response for templates/temp1"),
        ("compute", lambda: client.computeByID("comp1")[1], "Dummy response for computes/comp1"),
        ("docker-images", lambda: client.computeByIDDockerImages("comp1")[1], "Dummy response for computes/comp1/docker/images"),
        ("virtualbox-vms", lambda: client.computeByIDVirtualvoxVms("comp1")[1], "Dummy response for computes/comp1/virtualbox/vms"),
        ("vmware-vms", lambda: client.computeByIDVmwareVms("comp1")[1], "Dummy response for computes/comp1/vmware/vms"),
        ("appliance (one arg)", lambda: client.appliance("app1")[1], "Dummy response for appliances/app1"),
        ("pool", lambda: client.pool("pool1")[1], "Dummy response for pools/pool1"),
        ("pool-resources", lambda: client.poolResources("pool1")[1], "Dummy response for pools/pool1/resources"),
        ("drawings", lambda: client.drawings("proj1")[1], "Dummy response for projects/proj1/drawings"),
        ("symbol", lambda: client.symbol("symbol1")[1], "Dummy response for symbols/symbol1/raw"),
        ("acl-rule", lambda: client.aclById("rule1")[1], "Dummy response for access/acl/rule1"),
        ("links", lambda: client.links("proj1")[1], "Dummy response for projects/proj1/links"),
        ("nodes", lambda: client.nodes("proj1")[1], "Dummy response for projects/proj1/nodes"),

        # Two-argument methods
        ("node", lambda: client.nodeByID("proj1", "node1")[1], "Dummy response for projects/proj1/nodes/node1"),
        ("node-links", lambda: client.nodeLinksByID("proj1", "node1")[1], "Dummy response for projects/proj1/nodes/node1/links"),
        ("link", lambda: client.link("proj1", "link1")[1], "Dummy response for projects/proj1/links/link1"),
        ("link-filters", lambda: client.linkFilters("proj1", "link1")[1], "Dummy response for projects/proj1/links/link1/available_filters"),
        ("drawing (two args)", lambda: client.drawing("proj1", "draw1")[1], "Dummy response for projects/proj1/drawings/draw1"),
    ]

    for desc, func, expected in tests:
        run_test(desc, func, expected)

    # Test notifications and project_notifications separately (they don't return a value)
    print("Testing notifications...", end=" ")
    try:
        client.notifications(timeout_seconds=1)
        print(f"{GREEN}Success{RESET}")
    except Exception as e:
        print(f"{RED}Failed: Exception {e}{RESET}")

    print("Testing project_notifications...", end=" ")
    try:
        client.project_notifications("proj1", timeout_seconds=1)
        print(f"{GREEN}Success{RESET}")
    except Exception as e:
        print(f"{RED}Failed: Exception {e}{RESET}")

if __name__ == "__main__":
    main()
