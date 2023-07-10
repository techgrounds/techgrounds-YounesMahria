# Log [Juni 30 2023]

  

## Dagverslag (1 zin)
- De keypairs goed aanmaken en verbinden maken met web en management server.
  

## Obstakels
- De keypairs werden bij elke deploy gemaakt en dan verwijderd. 
- Kon geen verbinding maken met web en management server.

## Oplossingen
- De keypairs hadden nog 1 lijn code nodig om te voorkomen dat het wordt verwijderd.
- De twee servers op EC2 Instances waren op private en niet public subnet waardoor ze niet bereikbaar waren.

## Learnings
- CDK en CloudFormation kunnen anders de code logica opvatten. Wanneer CDK naar CloudFormation vertaald, dan kan de template net anders zijn omdat bij if else de code aanmaken er wel staat en bij else niet. Hierdoor komt CloudFormation in een conflict van het bestaan ervan.