# @hadespwnme
import requests

url = "https://leakosintapi.com/"
api_token = "8004396055:WjHNx9er"  # don't change
lang = "en"
limit = 1000

def fetchData(query):
    data = {
        "token": api_token,
        "request": query,
        "limit": limit,
        "lang": lang
    }
    try:
        response = requests.post(url, json=data).json()
        return response.get("List", {})
    except Exception as e:
        print("Can't connect to database.", e)
        return None

def formatData(data):
    output = ""
    no_results = False

    for key, value in data.items():
        records = value.get("Data", [])

        output += "\n===================================\n"
        output += f"📂 DATABASE: {key}\n"
        output += "===================================\n\n"

        if key == "No results found":
            no_results = True
            break
        else:
            for idx, record in enumerate(records, start=1):
                output += f"🔍 Result #{idx}\n"
                output += f"──────────────────────────\n"

                for field, val in record.items():
                    output += f"🔹 {field}: {val}\n"

                output += f"──────────────────────────\n\n"
            output += "===================================\n\n"
    
    return output, no_results

def main():
    try:
        while True:
            query = input("\n🔎 Input keyword for searching: ")
            data = fetchData(query)

            if data is None:
                continue

            result_text, no_results = formatData(data)
            print(result_text)

            if no_results:
                continue

            save = input("\n💾 Save the report? (y/n): ").strip().lower()
            if save in ["y", "yes"]:
                file_name = input("\n📁 Input file name: ").strip()
                try:
                    with open(file_name, "w", encoding="utf-8") as f:
                        f.write(result_text)
                    print(f"\n✅ Report saved as '{file_name}' successfully!")
                except Exception as e:
                    print(f"\n❌ Error saving file: {e}")

    except KeyboardInterrupt:
        print("\n\n🚪 Program dihentikan oleh pengguna. Keluar...\n")

if __name__ == "__main__":
    main()
