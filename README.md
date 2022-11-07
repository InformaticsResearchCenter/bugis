# bugis
blacksheep for GIS support
start apps 
```sh
pip install -r requirements.txt
uvicorn server:app --port 44777 --reload
```

## Example
just build your module in module folder, use static folder for save your data.
### Writing SHP
method POST : https://sheltered-fjord-41181.herokuapp.com/m/gis/SG/seletar/airport
with json body
```json
{
  "longitude" : 103.87068815153685,
  "latitude" : 1.4155690028533765,
  "name" : "seletar airport"
}
```
### Reading SHP
method GET : https://sheltered-fjord-41181.herokuapp.com/m/gis/SG/seletar/getairport/0
