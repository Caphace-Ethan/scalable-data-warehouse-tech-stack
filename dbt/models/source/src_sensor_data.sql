with source as (
  select * from {{ ref('all_sensor_data') }}
),

src_sensor_data as (
  select
    utc_time_id,
    source_id,
    high_quality_samples,
    samples_below_100pct_ff,
    samples_below_90pct_ff,
    samples_below_80pct_ff,
    samples_below_70pct_ff,
    samples_below_50pct_ff,
    samples_below_20pct_ff,
    samples_below_5pct_ff
  from source
)
select
  *
from src_sensor_data

