package me.nassim.androidApp

import android.annotation.SuppressLint
import android.content.Intent
import android.os.AsyncTask
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.ListView
import me.nassim.shared.Greeting
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import org.json.JSONArray
import java.net.HttpURLConnection
import java.net.URL

fun greet(): String {
    return Greeting().greeting()
}

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val url = "https://mysafeinfo.com/api/data?list=presidents&format=json"

        AsyncTaskHandleJson().execute(url)
    }

    @SuppressLint("StaticFieldLeak")
    inner class AsyncTaskHandleJson : AsyncTask<String, String, String>() {
        override fun doInBackground(vararg url: String?): String {
            val text: String
            val connection = URL(url[0]).openConnection() as HttpURLConnection
            try {
                connection.connect()
                text = connection.inputStream.use { it.reader().use{reader -> reader.readText()}}
            }finally {
                connection.disconnect()
            }
            return text
        }

        override fun onPostExecute(result: String?) {
            super.onPostExecute(result)
            handleJson(result)
        }
    }

    private fun handleJson(jsonString: String?) {

        val jsonArray = JSONArray(jsonString)

        val list = ArrayList<President>()

        for(i in 0 until jsonArray.length() ){
            val jsonObject = jsonArray.getJSONObject(i)

            list.add(
                President(
                jsonObject.getInt("ID"),
                jsonObject.getString("FullName"),
                jsonObject.getString("Party"),
                jsonObject.getString("Terms")
            )
            )
        }
        println(list)
        val moduleRecyclerView = this.findViewById<RecyclerView>(R.id.module_recyclerview)
        val adapter = ModuleAdapter(this,list)
        moduleRecyclerView.adapter = adapter
    }

    fun changeToCreation(view: View) {
        val intent = Intent(this, CreationDevis::class.java)
    }
}
