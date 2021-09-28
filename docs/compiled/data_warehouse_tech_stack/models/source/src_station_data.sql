with source as (
  select * from `sensor_data`.`I80_stations`
),

src_station_data as (
  select
    ID,
    Fwy,
    Dir,
    District,
    County,
    City,
    State_PM,
    `Length`,
    `Type`,
    Lanes,
    Latitude,
    Longitude,
    `Name`
  from source
)
select
  *
from src_station_data