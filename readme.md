# turret_resolver
**turret_resolver** is where the magic happens. All the resolving logic happens here. Decoupled from the server, this package allows DCCs to resolve turret queries without the overhead of the server logic, and to minimize impact when rolling out server and resolver updates. 

## Building
We use the [rez](https://github.com/nerdvegas/rez) build system at utsala, with the correct pacakge requirements, building this with rez should work straight out of the box.

Outside of rez, having the required software installed and correctly located in the `PATH` and `PYTHONPATH` environment variables should suffice.

### Requirements
 * python-2

## Contributing
We use turret across almost every aspect of our USD pipeline and are constantly fixing bugs and finding time to improve turret more and more. We are however, very open to external pull-requests, and growing turret into a more versatile and robust piece of software with your help. Feel free to get in contact directly or through these GitHub repos. We'd love to talk! 

