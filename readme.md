# turret_resolver
**turret_resolver** is the core resolving logic which converts turret uri queries into filepaths and vice versa. Decoupled from the server, this package allows DCCs to resolve turret queries without the overhead of the server logic, and to minimize impact when rolling out server and resolver updates. 

This is an example of a turrety uri query `tank:/s118/maya_publish_asset_cache_usd?Step=model&Task=model&asset_type=setPiece&version=latest&Asset=building01` we embed project year, asset meta data, and shotgun template in this one uri query. Of specific note are the `version` and `platform` uri paramaters. `version` can be set to a specific published version or the keyword `latest` can be used. And `platform` is an optional paramater which if specified as `windows` will return queries with the correct windows paths. The default platform is `linux`.

We also have included several convinience functions as part of **turret_resolver** which can assist in handling turret uri queries.

## Shotgun info
turret_resolver currently requires that project metadata be provided in a json file, found by the environment variable $SHOTGUN_INFO.  This json file defines various keys to inform turret_resolver about project names, ids, and roots.  

An example of a shotgun.json file is:

```
{
    "install":
    {
        "proj1": "/projects/jobs/proj1",
        "proj2": "/projects/jobs/proj2",
        "proj3": "/projects/jobs/proj3"
    },
    "project_roots":
    {
        "proj1": ["/projects/jobs/proj1", "/projects/wip/proj1"],
        "proj2": ["/projects/jobs/proj2", "/projects/wip/proj2"],
        "proj3": ["/projects/jobs/proj3", "/projects/wip/proj3"]
    },
    "platform":
    {
        "windows": "win32",
        "linux": "linux2",
        "osx": "darwin"
    },
    "id":
    {
        "proj1": "123",
        "proj2": "456",
        "proj3": "789"
    }
}
```
The `install` key defines where the shotgun config for the project can be found.  The `project_roots` key defines a list of roots for a given project (since a shotgun toolkit schema can accomodate multiple roots for a single project).  


## Building
We use the [rez](https://github.com/nerdvegas/rez) build system at utsala, with the correct pacakge requirements, building this with rez should work straight out of the box.

Outside of rez, having the required software installed and correctly located in the `PATH` and `PYTHONPATH` environment variables should suffice.

### Requirements
 * python-2

## Contributing
We use turret across almost every aspect of our USD pipeline and are constantly fixing bugs and finding time to improve turret more and more. We are however, very open to external pull-requests, and growing turret into a more versatile and robust piece of software with your help. Feel free to get in contact directly or through these GitHub repos. We'd love to talk! 

