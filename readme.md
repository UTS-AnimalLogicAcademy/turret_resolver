# turret_resolver
**turret_resolver** is the core resolving logic which converts turret uri queries into filepaths and vice versa. Decoupled from the server, this package allows DCCs to resolve turret queries without the overhead of the server logic, and to minimize impact when rolling out server and resolver updates. 

This is an example of a turrety uri query `tank:/s118/maya_publish_asset_cache_usd?Step=model&Task=model&asset_type=setPiece&version=latest&Asset=building01` we embed project year, asset meta data, and shotgun template in this one uri query. Of specific note are the `version` and `platform` uri paramaters. `version` can be set to a specific published version or the keyword `latest` can be used. And `platform` is an optional paramater which if specified as `windows` will return queries with the correct windows paths. The default platform is `linux`.

We also have included several convinience functions as part of **turret_resolver** which can assist in handling turret uri queries.

## Building
We use the [rez](https://github.com/nerdvegas/rez) build system at utsala, with the correct pacakge requirements, building this with rez should work straight out of the box.

Outside of rez, having the required software installed and correctly located in the `PATH` and `PYTHONPATH` environment variables should suffice.

### Requirements
 * python-2

## Contributing
We use turret across almost every aspect of our USD pipeline and are constantly fixing bugs and finding time to improve turret more and more. We are however, very open to external pull-requests, and growing turret into a more versatile and robust piece of software with your help. Feel free to get in contact directly or through these GitHub repos. We'd love to talk! 

