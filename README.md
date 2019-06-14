### Adding a custom Bro connection log (conn.log) template
#### Elasticsearch <= 6.7
Add a template using:

```bash
curl -H'Content-Type: application/json' -XPUT http://localhost:9200/_template/bro-conn-log_template?pretty -d @bro-template.json
```

#### Elasticsearch >= 6.8
Add a template using:

```bash
curl -H'Content-Type: application/json' -XPUT http://localhost:9200/index?pretty -d @index_template.json
```
