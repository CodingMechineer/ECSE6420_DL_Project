import fiftyone as fo
import fiftyone.zoo as foz

# The path to the source files
source_dir = "bdd100k"

dataset = foz.load_zoo_dataset(
    "bdd100k",
    split="test",
    source_dir=source_dir,
)

session = fo.launch_app(dataset, port=5151)