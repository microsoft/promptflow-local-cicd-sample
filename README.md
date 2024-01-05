# Integrate PromptFlow into a CI/CD pipeline (On-Agent)
> [!Note]
> This sample demonstrates adding PromptFlow evaluations in existing Python applications, including LangChain and others like Semantic Kernel's Python version. At present, it directly runs PromptFlow on the agent. It's ideal for smaller applications with an established deployment setup, looking to use PromptFlow solely for evaluation purposes. If you are looking for an end-to-end solution using PromptFlow, I recommend exploring the [LLMOps template repository on GitHub.](https://github.com/microsoft/llmops-promptflow-template/)

Every AI app should include evals! With [PromptFlow](https://microsoft.github.io/promptflow/), we ensure not only the functional correctness of our code but also the precision and reliability of AI inferences, preventing issues like hallucinations. For more information about PromptFlow, visit the [PromptFlow documentation](https://microsoft.github.io/promptflow/) and the [GitHub repository](https://github.com/microsoft/promptflow). 


## Getting Started with this Sample 🛠️

### Setting Up Azure Pipelines

To set up Azure Pipelines for this project:

1. **Create a Variable Group:** 
   - The pipeline depends on a specific variable group named `promptflow-evals`. 
   - Ensure this group includes all necessary variables, such as `DEPLOYMENT_NAME`, `AZURE_OPENAI_ENDPOINT`, and `AZURE_OPENAI_API_KEY`.

2. **Configure the Pipeline:**
   - Modify the `azure-pipelines.yaml` file according to your project's needs. 
   - This file outlines the build and test processes, integral to integrating PromptFlow evaluations into your CI/CD workflow.

3. **Run the Pipeline:**
   - Trigger the pipeline through Azure Pipelines.
   - Upon completion, the results of the PromptFlow evaluations will be accessible as an artifact.
   - Review this artifact for a detailed report of the evaluations.

### Using VS Code Extension for PromptFlow

VS Code, complemented by the PromptFlow extension, offers an intuitive environment for working with PromptFlow:

1. **Install Required Tools:**
   - Download and install the latest stable version of [VS Code](https://code.visualstudio.com/).
   - Add the [Python extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
   - Install the [PromptFlow extension for VS Code](https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow).

2. **Set Up Your Environment:**
   - Choose the appropriate Python interpreter in VS Code.
   - Use the visual editor to open `flow.dag.yaml` for an enhanced flow editing and testing experience.

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
