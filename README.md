# cs462-http-requests
Lab 2: HTTP Methods, Headers, and Return Codes Lab

Access http://ec2-52-23-154-187.compute-1.amazonaws.com/cgi-bin/test.cgi with query strings "repo", "search", or "face" to be redirected to a different site.

Test out printing the POST body with the following `curl` command:

    curl -H "Content-Type: application/json" -X POST -d '{"username":"xyz","password":"xyz"}' http://ec2-52-23-154-187.compute-1.amazonaws.com/cgi-bin/test.cgi?foo
