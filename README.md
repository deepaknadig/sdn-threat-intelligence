### Adding a custom Bro connection log (conn.log) template
Add a template using:

```bash
curl -H'Content-Type: application/json' -XPUT http://localhost:9200/_template/bro-conn-log_template?pretty -d @bro-template.json
```
