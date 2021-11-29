class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_account = defaultdict(list)
        ptr = 0
        for i in accounts:
            for j in range(1, len(i)):
                email_account[i[j]].append(ptr)
            ptr+=1

        def traverse(current_account):
            queue = [current_account]
            related_emails = set()
            curr = []
            while queue:
                # pop the account number
                ele = queue.pop()
                # add the current account as visited
                visited.add(ele)
                # print(visited)
                # add all its email to related_emails
                for email in accounts[ele][1:]:
                    if email not in related_emails:
                        related_emails.add(email)
                        # add all the accounts of the same email to process next
                        # print(related_emails)
                        for ac in email_account[email]:
                            if ac not in visited:
                                curr.append(ac)
                if not queue:
                    if not curr:
                        # print(related_emails)
                        return related_emails
                    else:
                        queue = curr
                        curr = []

        visited = set()
        res = []
        for i in range(len(accounts)):
            if i not in visited:
                # print(":))")
                rel = traverse(i)
                # print(rel)
                res.append([accounts[i][0]]+sorted(list(rel)))
                # print(res)
        return res
        