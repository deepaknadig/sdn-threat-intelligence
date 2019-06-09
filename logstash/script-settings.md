## Settings to Increase script compilation rates.

```
PUT _cluster/settings
{
 "transient" : {
    "script.max_compilations_rate" : "15/1m"
 }
}
```
**Note** Use script parameters instead.