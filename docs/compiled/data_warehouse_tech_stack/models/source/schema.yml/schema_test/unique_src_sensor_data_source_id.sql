
    
    



select count(*) as validation_errors
from (

    select
        source_id

    from `sensor_data`.`src_sensor_data`
    where source_id is not null
    group by source_id
    having count(*) > 1

) validation_errors


