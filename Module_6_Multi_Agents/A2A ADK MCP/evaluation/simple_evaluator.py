import json
import asyncio
import re
from typing import Dict, List, Any
from query_MCP_ADK_A2A import analyze_salary_data_async

class SimpleEvaluator:
    """A simplified evaluator for testing the multi-agent security system."""

    def __init__(self, scenarios_file="test_scenarios.json", config_file="test_config.json"):
        """Initialize the evaluator with test scenarios and configuration."""
        # Load test scenarios
        with open(scenarios_file, 'r') as f:
            self.scenarios = json.load(f)

        # Load configuration
        with open(config_file, 'r') as f:
            self.config = json.load(f)

        # Initialize results
        self.results = {
            "summary": {
                "total": 0,
                "passed": 0,
                "failed": 0
            },
            "details": []
        }

    async def evaluate_query(self, query: str, expected_outcome: str, test_name: str) -> Dict[str, Any]:
        """Evaluate a single query and return the results."""
        print(f"\nTesting: {test_name}")
        print(f"Query: {query}")
        print(f"Expected outcome: {expected_outcome}")

        # Call your multi-agent system
        try:
            # Use your existing function to process the query
            result = await analyze_salary_data_async(query)

            # Fix tuple format if needed and configured
            if self.config.get("fix_tuple_format", False) and isinstance(result, str):
                # Extract number from tuple format like (75454.38888888889,)
                tuple_match = re.search(r'\(([\d\.]+),\)', result)
                if tuple_match:
                    result = tuple_match.group(1)

            # Determine actual outcome
            if "blocked" in result.lower() or "security concerns" in result.lower():
                actual_outcome = "BLOCKED"
            else:
                actual_outcome = "PASSED"

            # Check if test passed
            test_passed = (actual_outcome == expected_outcome)

            # Build result details
            test_result = {
                "name": test_name,
                "query": query,
                "expected_outcome": expected_outcome,
                "actual_outcome": actual_outcome,
                "response": result,
                "passed": test_passed
            }

            return test_result

        except Exception as e:
            # Handle any exceptions
            print(f"Error: {str(e)}")
            return {
                "name": test_name,
                "query": query,
                "expected_outcome": expected_outcome,
                "actual_outcome": "ERROR",
                "response": f"Error: {str(e)}",
                "passed": False
            }

    async def run_evaluation(self):
        """Run all test scenarios and generate a report."""
        print("Starting evaluation...")

        # Process all scenarios
        all_scenarios = []
        all_scenarios.extend([{"category": "malicious", **s} for s in self.scenarios["malicious_queries"]])
        all_scenarios.extend([{"category": "legitimate", **s} for s in self.scenarios["legitimate_queries"]])

        # Initialize counters
        total = len(all_scenarios)
        passed = 0

        # Process each scenario
        for scenario in all_scenarios:
            # Evaluate the query
            result = await self.evaluate_query(
                query=scenario["query"],
                expected_outcome=scenario["expected_outcome"],
                test_name=f"{scenario['category']}_{scenario['name']}"
            )

            # Update counters
            if result["passed"]:
                passed += 1
                print("✅ Test passed!")
            else:
                print("❌ Test failed!")
                print(f"  Expected: {result['expected_outcome']}")
                print(f"  Actual: {result['actual_outcome']}")
                print(f"  Response: {result['response']}")

            # Add to results
            self.results["details"].append(result)

        # Update summary
        self.results["summary"]["total"] = total
        self.results["summary"]["passed"] = passed
        self.results["summary"]["failed"] = total - passed

        # Save results
        if "save_results_to" in self.config:
            with open(self.config["save_results_to"], 'w') as f:
                json.dump(self.results, f, indent=2)
                print(f"\nResults saved to {self.config['save_results_to']}")

        # Display summary
        print("\n===== EVALUATION SUMMARY =====")
        print(f"Total tests: {total}")
        print(f"Passed: {passed} ({passed/total*100:.1f}%)")
        print(f"Failed: {total - passed} ({(total-passed)/total*100:.1f}%)")

        return self.results

# Example usage
async def main():
    evaluator = SimpleEvaluator()
    await evaluator.run_evaluation()

if __name__ == "__main__":
    asyncio.run(main())
