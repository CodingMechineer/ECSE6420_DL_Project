import fiftyone as fo
import fiftyone.zoo as foz

# The path to the source files
source_dir = "201 - Deep Learning -/100 - Project/bdd100k"

dataset = foz.load_zoo_dataset(
    "bdd100k",
    split="validation",
    source_dir=source_dir,
)

session = fo.launch_app(dataset)