To initiate the demo.py script, a docker instance needs to be created using the following command:

```bash
docker compose up -d
```

Subsequently, the `demo.py script can be executed by invoking the command:

```bash
python demo.py config.yml
```

It is mandatory that the YAML configuration file adheres to the following format:

```yaml
datasource_url: "postgresql://username:password@host:port/cars" 
url: "https://host:port/endpoint"
```