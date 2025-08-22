from llama_stack.providers.datatypes import (
    AdapterSpec,
    Api,
    ProviderSpec,
    remote_provider_spec,
)


def get_provider_spec() -> ProviderSpec:
    return remote_provider_spec(
        api=Api.eval,
        adapter=AdapterSpec(
            adapter_type="lmeval",
            pip_packages=["kubernetes"],
            config_class="lmeval.config.LMEvalBenchmarkConfig",
            module="lmeval",
        ),
    )
